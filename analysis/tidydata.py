import pandas as pd
import numpy as np
from datetime import datetime
import os
import re
import json

WD = os.getcwd().split("describe/")[0] + "describe/"
SURVEY_SIZE = 15
TRIAL_SIZE = 44


class Experiment:
    def __init__(self, file_name):
        """Input: .csv file created by Pavlovia/JSpsych"""
        # Log sucess/errors
        self.success = []
        self.errors = []
        self.file_name = file_name
        # Shorten file name
        self.tmp_fn = re.sub("SESSION_|.csv", "", self.file_name)
        # Get participant information from filename
        (
            self.study_name,
            self.part_id,
            self.date,
            self.time,
            self.tsec,
            self.tms,
        ) = re.split("_|\.", self.tmp_fn)

    def get_data(self):
        """Open .csv file; check that resources were loaded properly;
        verify consent was acknowledged; read trial information"""
        print(f" -- Getting data: {self.file_name}")
        self.raw = pd.read_csv(WD + "data/" + self.file_name)

        # Verify resources loaded properly
        if self.raw["success"].isin([True]).any():
            self.success.append("Preload OK")
        else:
            self.errors.append("Error: experiment listed with no preload")

        # Verify consent form is complete
        if self.raw["consent"].isin(["complete"]).any():
            self.success.append("Consent complete")
        else:
            self.errors.append("Error: experiment does not have signed consent")

        # Get survey responses  --  Trial 6 are the demographic survey responses
        self.raw_survey = self.raw[self.raw["trial_index"].isin([6])][
            "response"
        ].values[0]
        self.dct_survey = json.loads(self.raw_survey)
        # Filter non-numeric
        self.dct_survey["q00_age"] = re.sub("\D", "", self.dct_survey["q00_age"])
        self.dct_survey["q07_music_train"] = re.sub(
            "\D", "", self.dct_survey["q07_music_train"]
        )

        if len(self.dct_survey) == SURVEY_SIZE:
            self.success.append("Survey complete")
        else:
            self.errors.append(
                "Error: survey incomplete: ", len(self.dct_survey), "/", SURVEY_SIZE
            )

        # Get trial responses
        self.raw_trials_subset = self.raw[
            # Edit this line
            self.raw["trial_index"].isin(np.arange(9, 9 + TRIAL_SIZE * 2, 2))
        ]
        self.dct_trials = []

        # Get meta-survey
        self.raw_meta_survey = self.raw[self.raw["trial_index"].isin([97])][
            "response"
        ].values[0]
        self.dct_meta_survey = json.loads(self.raw_meta_survey)

        ### =================== Most edits here! ========================== ###
        complete_trials = 0
        for i, (j, t) in enumerate(self.raw_trials_subset.iterrows()):
            # There are two response rows in the csv, skip all but the 'replays'
            #   from the second row
            if pd.isnull(t["response"]):
                continue
            elif (
                pd.isnull(self.raw_trials_subset.loc[j + 1, "response"])
                and self.raw_trials_subset.loc[j + 1, "trial_index"] == t["trial_index"]
            ):
                t["replays"] = self.raw_trials_subset.loc[j + 1, "replays"]

            # Optional - print row information
            # print(f"\nindex: {i} \nj: {j}, \nt: {t}")

            # Count trial (not duplicates)
            complete_trials += 1

            # Response
            tmp_dct = json.loads(t["response"])
            tmp_dct.pop("space")
            tmp_dct.pop("replay")

            # Trial info
            tmp_dct["id_file"] = self.tmp_fn
            tmp_dct["id_stim"] = t["sound"].replace(".mp3", "").rsplit("/")[-1]
            tmp_dct["replayed"] = t["replays"]
            tmp_dct["trial_num"] = complete_trials
            tmp_dct["trial_time_elapsed"] = t["time_elapsed"]

            # # Probably do not need to change
            tmp_dct["study"] = self.study_name
            tmp_dct["part_id"] = self.part_id
            tmp_dct["date"] = self.date
            tmp_dct["hour"] = self.time.split("h")[0]
            tmp_dct["min"] = self.time.split("h")[1]
            tmp_dct["sec"] = self.tsec
            tmp_dct["ms"] = self.tms
            tmp_dct["finish_time"] = self.raw.iloc[-1]["time_elapsed"]
            tmp_dct["success_msg"] = "/".join(self.success)
            tmp_dct["error_msg"] = "/".join(self.errors)

            # # Add participant information
            tmp_dct.update(self.dct_survey)
            # # Add survey information
            tmp_dct["rate_difficulty"] = self.dct_meta_survey["rate_difficulty"]
            tmp_dct["rate_training"] = self.dct_meta_survey["rate_training"]
            tmp_dct.update(self.dct_meta_survey["P0_Q2"])
            tmp_dct.update(self.dct_meta_survey["P0_Q3"])

            self.dct_trials.append(tmp_dct)

        if len(self.dct_trials) == TRIAL_SIZE:
            self.success.append("Trials complete")
        else:
            self.errors.append(
                "Error: trials incomplete: ", len(self.dct_trials), "/", TRIAL_SIZE
            )

        # Create table
        self.dat_full = pd.DataFrame(
            self.dct_trials,
            index=[(x["id_file"], x["id_stim"]) for x in self.dct_trials],
        )
        ### =================== ================ ========================== ###

        # Print success/errors
        print("Successful: ", self.success, "Errors: ", self.errors)


# Print info while working...
print(f"~~ Get and clean data ~~\n", f'\t\tLooking for data in: {WD + "data/"}')
data_files = os.listdir(WD + "data/")
print(f"\t\tFound: {len(data_files)} data files")

# Generate list of participant experiments from files
part_list = [Experiment(par) for par in data_files]

# Empty df for now
all_data_clean = pd.DataFrame()

# Call get_data method, combine to full data file
for part in part_list:
    part.get_data()
    all_data_clean = pd.concat([all_data_clean, part.dat_full])

# Name the file with date time so we know whats most up-to-date; write
current_date_time = datetime.now().strftime("%Y-%m-%d-%H%M")
all_data_clean.to_csv(WD + "analysis/" + current_date_time + ".csv", index_label="idx")
