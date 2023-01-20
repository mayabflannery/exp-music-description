/* Define instructions trial */
var postInstructions = {
	type: jsPsychInstructions,
	pages: [
		'The study is almost done. The following page will present<br>\
		a few questions regarding the listening task you just completed.'
	],
	button_label_next: "Continue",
	button_label_previous: "Back",
	show_clickable_nav: true,
    on_finish: function () {
        overall_trial++;
        jsPsych.setProgressBar(overall_trial / all_trials);
    }
};
all_trials++;
timeline.push(postInstructions);
