import pandas as pd

# Read items from .csv
qs = pd.read_csv("../resources/text/personality.csv", index_col="NUM")
errors = 0

# Add helper columns for scoring direction, factor name, and facet
qs["SCORE"] = ["pos" if x.startswith("+") else "neg" for x in qs["KEY"]]
qs["FACTOR"] = [x.strip("+")[0] for x in qs["KEY"]]
qs["FACET"] = [x.strip("+")[1] for x in qs["KEY"]]

qs.sort_index(inplace=True)

qt_instructions = "Describe yourself as you generally are now, not as you wish to be in the future. Describe yourself as you honestly see yourself, in relation to other people you know of the same sex as you are, and roughly your same age. So that you can describe yourself in an honest manner, your responses will be kept in absolute confidence. Indicate for each statement whether it is 1. Very Inaccurate, 2. Moderately Inaccurate, 3. Neither Accurate Nor Inaccurate, 4. Moderately Accurate, or 5. Very Accurate as a description of you."

with open("personality-trials.js", "w") as f:
    f.write(f"/* ----- Created with mk-personality.py ----- */")

    # Positive scoring
    f.write(
        "\nvar likert_positive = ["
        + "\n\t{value: 1, text: 'Very Inaccurate'},"
        + "\n\t{value: 2, text: 'Moderately Inaccurate'},"
        + "\n\t{value: 3, text: 'Neither Accurate Nor Inaccurate'},"
        + "\n\t{value: 4, text: 'Moderately Accurate'},"
        + "\n\t{value: 5, text: 'Very Accurate'}"
        + "\n]\n"
    )

    # Negative scoring
    f.write(
        "\nvar likert_negative = ["
        + "\n\t{value: 5, text: 'Very Inaccurate'},"
        + "\n\t{value: 4, text: 'Moderately Inaccurate'},"
        + "\n\t{value: 3, text: 'Neither Accurate Nor Inaccurate'},"
        + "\n\t{value: 2, text: 'Moderately Accurate'},"
        + "\n\t{value: 1, text: 'Very Accurate'}"
        + "\n]\n"
    )

    # Begin file
    f.write(
        "\nvar personalitytrial = {"
        + "\n\ttype: jsPsychSurvey,"
        + "\n\ttitle: 'Personality questionnaire',"
        + "\n\tbutton_label_next: 'Next page',"
        + "\n\tbutton_label_previous: 'Previous page',"
        + "\n\tbutton_label_finish: 'Submit',"
        + "\n\tshow_question_numbers: 'onPage',"
        + "\n\tpages: ["
    )

    # Write questions
    for i in qs.index:
        if i == 1:
            print(f"i = {i}: Start")
            f.write(
                "\n\t["
                + "\n\t\t{\n\t\t\ttype: 'html',"
                + f"\n\t\t\tprompt: '{qt_instructions}',"
                + "\n\t\t},"
            )
        elif i == len(qs):
            print(f"i = {i}: End")
            f.write("\n\t]")
        elif i % 5 == 0:
            print(f"i = {i}: new page")
            f.write(
                "\n\t],\n\t["
                + "\n\t\t{\n\t\t\ttype: 'html',"
                + f"\n\t\t\tprompt: '{qt_instructions}',"
                + "\n\t\t},"
                + "\n\t\t{"
            )
        else:
            print(f"i = {i}: q")
            f.write("\n\t\t{")

        st_name = f"\n\t\t\tname: '{i:03d}_{qs.loc[i, 'KEY']}',"
        st_prompt = f"\n\t\t\tprompt: '{qs.loc[i, 'ITEM']}',"
        st_type = "\n\t\t\ttype: 'likert',"
        st_req = "\n\t\t\trequired: true,"

        if qs.loc[i, "SCORE"] == "pos":
            st_likert = "\n\t\t\tlikert_scale_values: likert_positive,"
        elif qs.loc[i, "SCORE"] == "neg":
            st_likert = "\n\t\t\tlikert_scale_values: likert_negative,"
        else:
            print("ERROR!")
            errors += 1

        f.write(st_name + st_type + st_prompt + st_req + st_likert + "\n\t\t},")

    # End file
    f.write(
        "\n\t]"
        + "\n};"
        + "\ntimeline.push(personalitytrial);"
        + "\n/* ----- End of mk-personality.py"
        + f"\n\t\tfinished with {errors} errors ----- */"
    )
