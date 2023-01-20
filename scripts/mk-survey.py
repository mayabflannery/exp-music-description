import pandas as pd

questionnaire_name = "demographic"

csv_name = "resources/text/" + questionnaire_name + ".csv"

qd = pd.read_csv(csv_name)

errors = 0

with open("out", "w") as f:
    # Start survey
    f.write(
        f"/* ----- Survey: {questionnaire_name} ----- \n" + 
        "\t\tGenerated with mk-survey.py */\n" +
        "var " + questionnaire_name + " = {\n" +
        "\ttype: jsPsychSurvey,\n" +
        "\tpages: [\n"
    )

    # Parse csv by row
    for i in range(0, len(qd)):
        st_name = f"\t\tname: `q{i:02d}_{qd.loc[i, 'name']}`,\n"
        st_type = f"\t\ttype: `{'text' if qd.loc[i, 'type'] == 'numeric' else qd.loc[i, 'type']}`,\n"
        st_prompt = f"\t\tprompt: `{qd.loc[i, 'prompt']}`,\n"
        st_place = f"\t\tplaceholder: `{qd.loc[i, 'placeholder']}`,\n"
        st_options = f"\t\toptions: {qd.loc[i, 'options']},\n"
        st_cols = f"\t\ttextbox_columns: 5, \n"
        st_required = f"\t\trequired: {str(qd.loc[i, 'required']).lower()}\n"

        if qd.loc[i, "type"] == "numeric":
            f.write("\t[{\n" +
                st_name + st_type + st_prompt + st_cols + st_required +
                "\t}],\n"
            )
        elif qd.loc[i, "type"] == "text":
            f.write("\t[{\n" +
                st_name + st_type + st_prompt + st_place + st_required +
                "\t}],\n"
            )
        elif qd.loc[i, "type"] == "multi-choice":
            f.write("\t[{\n" +
                st_name + st_type + st_prompt + st_options + st_required +
                "\t}],\n"   
            )
        else:
            errors += 1
            print("Error in row: ", i, "\n\tUnknown type: ", qd.loc[i, 'type'])
            f.write(
                f"/* ----- ERROR in row: {i} ------ \n" +
                f"\t\tType: {qd.loc[i, 'type']} is not valid! */\n"
                )

    # Close survey
    f.write(
        "\t],\n" +
        "\ttitle: '" + questionnaire_name + " questionnaire',\n" +
        "\tbutton_label_next: 'Continue',\n" +
        "\tbutton_label_back: 'Previous',\n" +
        "\tbutton_label_finish: 'Submit',\n" +
        "\tshow_question_numbers: 'onPage'\n" +
        "};\n" +
        "timeline.push(" + questionnaire_name + ");\n" +
        f"/* ----- End of survey section [{errors} errors] ----- */\n"
    )