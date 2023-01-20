import os
import re
import pandas as pd
import numpy as np

USERPATH = os.path.expanduser("~")

searchLocation = USERPATH + "/Music/describeV1/"
# outputLocation = "../resources/music/"
outputLocation = USERPATH + "/projects/music-preference/describe/scripts/output/"


validTypes = ["flac", "mp3", "ogg", "opus"]

try:
    conf_tab = pd.read_csv(searchLocation + "makeStimuli.csv")
    print(f"Found stimuli configuration for {len(conf_tab)} files")
except FileNotFoundError:
    print(f"Could not find existing stimuli configuration")
    conf_tab = pd.DataFrame()

inputFiles = os.listdir(searchLocation)
print(f"Found {len(inputFiles)} files in {searchLocation}")
id_tab = pd.DataFrame({"s_input": inputFiles})
id_tab = id_tab[id_tab["s_input"].str.contains("|".join(validTypes))]
print(f" > There are {len(id_tab)} valid music files")


if conf_tab.empty:
    print("Creating new configuration file")
    # Clip start position
    id_tab["s_from"] = [np.nan] * len(id_tab)
    # Clip end position
    id_tab["s_to"] = [np.nan] * len(id_tab)
    # Placeholder for loudnorm filter
    id_tab["loudnorm"] = [np.nan] * len(id_tab)
    # Placeholder for loudnorm filter
    id_tab["volume_mod"] = [np.nan] * len(id_tab)
    # Make a clean output file name
    newnames = []
    sharenames = []
    for si in id_tab["s_input"]:
        try:
            s_name = re.search("\[...........\]", si)[0].strip("[]")
        except TypeError:
            print("ERROR: Fix song name!")
        sharenames.append(s_name)
        excludes = "\s|\." + "|\.".join(validTypes) + "|\[" + s_name + "\]"
        n_name = re.sub(excludes, "", si).lower()
        newnames.append(n_name)
    id_tab["s_output"] = newnames
    id_tab["s_name"] = sharenames
    id_tab.to_csv(searchLocation + "makeStimuli.csv")

# https://ffmpeg.org/ffmpeg-filters.html#afade-1
# ffmpeg -ss 10 -to 20 -i "input.mp3" -af "afade=t=in:ss=0:d=1,afade=t=out:st=9:d=1" "output.mp3"
# ss = start sample at 10s; to = time out (end) at 20s;
# -i =input file
# -af =audio filter; afade, t = type (in/out); d = duration (of fade)
s_fade_d = 1
s_out_type = "mp3"

if not conf_tab.empty:
    cont = True
    # Check for new entries
    if conf_tab["s_input"].isna().any():
        print("ERROR: Edit configure file to include valid input entries")
        cont = False
    # Check for valid clip length
    if conf_tab["s_from"].isna().any():
        print(
            "ERROR: Edit configure file to include valid 's_from' position for all songs"
        )
        cont = False
    if conf_tab["s_to"].isna().any():
        print(
            "ERROR: Edit configure file to include valid 's_to' position for all songs"
        )
        cont = False

    if cont:
        for i in range(len(conf_tab)):
            if conf_tab.loc[i, "loudnorm"] == "NL":
                loudness_normalization = ""
            else:
                loudness_normalization = ", loudnorm"

            # Generate command
            command = str(
                # cut from _ to _
                f"ffmpeg -ss {conf_tab.loc[i, 's_from']} -to {conf_tab.loc[i, 's_to']}"
                +
                # name of the input file
                f" -i '{searchLocation + conf_tab.loc[i, 's_input']}'"
                +
                # add fade in to beginning of clip
                f" -af 'afade=t=in:ss={0}:d={s_fade_d}"
                +
                # add fade out to end of clip
                f", afade=t=out:st={conf_tab.loc[i, 's_to'] - conf_tab.loc[i, 's_from'] - 1}:d={s_fade_d}"
                +
                # normalize the loudness of track to ---?
                # -docs: https://ffmpeg.org/ffmpeg-all.html#loudnorm
                loudness_normalization
                +
                # add fade out to end of clip
                f", volume={conf_tab.loc[i, 'volume_mod']}dB"
                +
                # name of outpout file, overwrite automatically
                f"' '{outputLocation + conf_tab.loc[i, 's_output'] + '.' + s_out_type}' -y"
            )
            print(command)
            os.system(command)
        conf_tab.to_csv(outputLocation + "music-list.csv")
