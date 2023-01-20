/* ----- Survey: demographic ----- 
		Generated with mk-survey.py */
var demographic = {
	type: jsPsychSurvey,
	pages: [
		[{
			name: `q00_age`,
			type: `text`,
			prompt: `What is your age?`,
			textbox_columns: 5,
			required: true
		}],
		[{
			name: `q01_hand`,
			type: `multi-choice`,
			prompt: `What is your handedness?`,
			options: ["Left", "Right", "n/a"],
			required: true
		}],
		[{
			name: `q02_colour`,
			type: `multi-choice`,
			prompt: `Do you have colour blindness?`,
			options: ["Yes", "No", "n/a"],
			required: true
		}],
		[{
			name: `q03_gender`,
			type: `multi-choice`,
			prompt: `What is your gender?`,
			options: ["Male", "Female", "Transgender", "Non-binary", "n/a"],
			required: true
		}],
		[{
			name: `q04_dance_train`,
			type: `text`,
			prompt: `Have you ever had any formal dance training?
If no, enter 0.
If yes, enter how many years of training.`,
			textbox_columns: 5,
			required: true
		}],
		[{
			name: `q05_dance_freq`,
			type: `multi-choice`,
			prompt: `Approximately how often do you dance? Once a:`,
			options: ["Never", "Monthly", "Weekly", "Daily", "n/a"],
			required: true
		}],
		[{
			name: `q06_dance_style`,
			type: `text`,
			prompt: `What style(s) do you dance?`,
			placeholder: `ex. Latin, Ballet, etc.`,
			required: false
		}],
		[{
			name: `q07_music_train`,
			type: `text`,
			prompt: `Have you ever had any formal music training?
If no, enter 0.
If yes, enter how many years of training.`,
			textbox_columns: 5,
			required: true
		}],
		[{
			name: `q08_music_instr`,
			type: `multi-choice`,
			prompt: `Do you play a musical instrument and/or sing?`,
			options: ["Yes", "No"],
			required: true
		}],
		[{
			name: `q09_music_type`,
			type: `text`,
			prompt: `What is your principle instrument?`,
			placeholder: `ex. Piano`,
			required: false
		}],
		[{
			name: `q10_music_age`,
			type: `text`,
			prompt: `At what age did you start playing?`,
			textbox_columns: 5,
			required: false
		}],
		[{
			name: `q11_music_freq`,
			type: `text`,
			prompt: `Including time spent rehearsing, approximately 
how many hours a week do you play/sing?`,
			textbox_columns: 5,
			required: true
		}],
		[{
			name: `q12_music_play`,
			type: `text`,
			prompt: `What type of music do you usually play? `,
			placeholder: `ex. Classical, Pop, etc.`,
			required: false
		}],
		[{
			name: `q13_music_listen`,
			type: `text`,
			prompt: `How many hours per week do you listen to music?`,
			textbox_columns: 5,
			required: true
		}],
		[{
			name: `q14_music_genre`,
			type: `text`,
			prompt: `What types of music do you listen to?`,
			placeholder: `ex. Classical, Pop, etc.`,
			required: false
		}],
	],
	title: 'Demographic questionnaire',
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
timeline.push(demographic);
/* ----- End of survey section [0 errors] ----- */
