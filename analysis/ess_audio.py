# =============================================================================
# Extract all music features
# =============================================================================
# https://essentia.upf.edu/streaming_extractor_music.html
# https://essentia.upf.edu/reference/std_MusicExtractor.htmf

import os
import re
import json
import pandas as pd
import numpy as np
import essentia
from essentia.standard import *

# Search directory for audio files
AUDIO_FOLDER = "../analysis/test/stimuli/"
JSON_FOLDER = "../analysis/test/json/"


audio_files = [x for x in os.listdir(AUDIO_FOLDER) if x.endswith(".mp3")]
json_files = [x for x in os.listdir(JSON_FOLDER) if x.endswith(".json")]


def extract_from_audio(audio_files):
    for i in audio_files:
        extract = MusicExtractor()
        features, frames = extract.compute(AUDIO_FOLDER + i)
        print(f"Extract features: {i}")
        # https://essentia.upf.edu/reference/std_YamlOutput.html
        YamlOutput(filename=i.removesuffix(".mp3") + ".json", format="json")(features)


def analyse_from_json(json_files):
    # https://docs.python.org/3/library/json.html?highlight=json#module-json
    dat = pd.DataFrame()
    for i in json_files:
        with open(JSON_FOLDER + i) as f:
            rd = json.load(f)
            # print(json.dumps(rd, indent=4))
            tmpd = pd.DataFrame(
                {
                    "name": [i.removesuffix(".json")],
                    "length": [rd["metadata"]["audio_properties"]["length"]],
                    "avg_loud": [rd["lowlevel"]["average_loudness"]],
                    "speed_bpm": [rd["rhythm"]["bpm"]],
                    "speed_rate": [rd["rhythm"]["onset_rate"]],
                    "artic": [""],
                    "register": [""],
                    "texture": [""],
                    "timbre_centroid": [rd["lowlevel"]["spectral_centroid"]["mean"]],
                    "timbre_complexity": [
                        rd["lowlevel"]["spectral_complexity"]["mean"]
                    ],
                    "timbre_decrease": [rd["lowlevel"]["spectral_decrease"]["mean"]],
                    "timbre_energy": [rd["lowlevel"]["spectral_energy"]["mean"]],
                    "timbre_rolloff": [rd["lowlevel"]["spectral_rolloff"]["mean"]],
                    "dynamic": [rd["lowlevel"]["dynamic_complexity"]],
                    "key_ekt": [
                        rd["tonal"]["key_edma"]["key"]
                        + "/"
                        + rd["tonal"]["key_krumhansl"]["key"]
                        + "/"
                        + rd["tonal"]["key_temperley"]["key"]
                    ],
                    "scale_ekt": [
                        rd["tonal"]["key_edma"]["scale"]
                        + "/"
                        + rd["tonal"]["key_krumhansl"]["scale"]
                        + "/"
                        + rd["tonal"]["key_temperley"]["scale"]
                    ],
                }
            )
            dat = pd.concat([dat, tmpd])
    print(dat)


# extract_from_audio(audio_files)
analyse_from_json(json_files)


# with open("analysis_notes.org", "w") as f:
#     for j in features.descriptorNames():
#         print(f"* Feature: {j} ", file=f)
#         print(type(features[j]), file=f)
#         print(features[j], file=f)

# print(dat)
