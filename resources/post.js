/* ----- Survey: demographic ----- */
var post = {
	type: jsPsychSurvey,
	title: 'Summary questionnaire',
	pages: [
		[
            {
                name: `rate_difficulty`,
                type: `multi-choice`,
                prompt: `How difficult was the listening task?`,
                options: ["Very easy", "Easy", "Average", "Difficult", "Very difficult"],
                columns: 5,
                required: true
            },
            {
                name: `rate_training`,
                type: `multi-choice`,
                prompt: `Did you find the musical term definitions and examples helpful?`,
                options: ["Not at all helpful", "Somewhat helpful", "Very helpful", "They made no difference", "I skipped the examples"],
                columns: 1,
                required: true
            },
            {
                type: `likert-table`,
                prompt: `How would you rate your understanding of each of the musical terms?`,
                statements: [
                    {prompt: "Speed", name: "understand_tempo"},
                    {prompt: "Loudness", name: "understand_dynamic"},
                    {prompt: "Register", name: "understand_register"},
                    {prompt: "Articulation", name: "understand_articulation"},
                    {prompt: "Texture", name: "understand_texture"},
                    {prompt: "Timbre", name: "understand_timbre"},
                ],
                options: ["Poor", "Below average", "Average", "Good", "Excellent"],
                required: true
            },
            {
                type: `likert-table`,
                prompt: `How confident were you in the responses you provided for:`,
                statements: [
                    {prompt: "Speed", name: "confidence_tempo"},
                    {prompt: "Loudness", name: "confidence_dynamic"},
                    {prompt: "Register", name: "confidence_register"},
                    {prompt: "Articulation", name: "confidence_articulation"},
                    {prompt: "Texture", name: "confidence_texture"},
                    {prompt: "Timbre", name: "confidence_timbre"},
                ],
                options: ["Not confident", "Somewhat confident", "Confident", "Very confident"],
                required: true
            },
            {
                name: `text_feedback`,
                type: `text`,
                prompt: `Do you have any other feedback that you would like to submit?`,
                placeholder: `Type your feedback here`,
                textbox_columns: 50,
                textbox_rows: 3,
                required: false
            },
        ],
	],
	button_label_next: 'Continue',
	button_label_back: 'Previous',
	button_label_finish: 'Submit',
	show_question_numbers: 'onPage',
    on_finish: function () {
        overall_trial++;
        jsPsych.setProgressBar(overall_trial / all_trials);
        }
};
all_trials++;
timeline.push(post);
