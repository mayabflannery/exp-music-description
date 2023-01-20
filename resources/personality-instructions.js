/* Define instructions trial */
var ins_pers = {
	type: jsPsychInstructions,
	pages: [
		'The following section is a personality questionnaire.<br>\
		Please read the prompt at the top of each page and answer <br>\
		each question to the best of your ability.',
        'Press <b>Continue</B> to start the questionnaire'
	],
	button_label_next: "Continue",
	button_label_previous: "Back",
	show_clickable_nav: true
};
timeline.push(ins_pers);
console.log("Loaded personality instructions");
