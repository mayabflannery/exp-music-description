/* ----- PreloadExamples Audio ----- */
var exampleFiles = [
/* =====================  List all stimuli here  ========================== */
"resources/examples/s1_articulation_smooth.mp3",
"resources/examples/s1_articulation_spiky.mp3",
"resources/examples/s1_register_high.mp3",
"resources/examples/s1_register_low.mp3",
"resources/examples/s3_dynamic_loud.mp3",
"resources/examples/s3_dynamic_soft.mp3",
"resources/examples/s4_speed_fast.mp3",
"resources/examples/s4_speed_slow.mp3",
"resources/examples/s6_timbre_bright.mp3",
"resources/examples/s6_timbre_dark.mp3",
"resources/examples/s7_texture_dense.mp3",
"resources/examples/s7_texture_sparse.mp3"
/* ========================  End stimuli list  ============================ */
];

var current_stimulus = null;
var replays = 0;

/*  PreloadExamples audio files  */
var preloadExamples = {
    type: jsPsychPreload,
    audio: exampleFiles,
    show_progress_bar: true,
    message: "Please wait for the experiment to load.",
    error_message: "The experiment failed to load!",
    max_load_time: 10000,
    show_detailed_errors: true,
};
/* Add preloadExamples to -beginning- of timeline with unshift */
timeline.unshift(preloadExamples);

/* Define instructions trial */
var instructions = {
	type: jsPsychInstructions,
	pages: [

'The following section will introduce a few musical terms<br>\
to help you complete the listening task.<br><br>\
You will have a chance to listen to examples of these musical terms.<br><br>\
You will also be able to refer back to these examples as you<br>\
complete the rest of the study.',

/* SPEED */
'<h1>1. Speed</h1>This refers to your perception of the music\'s tempo (i.e., beat velocity).\
<br>Your responses can range from: very slow to very fast.\
<br><br>Examples:\
<br>Slow music<br><audio controls src="resources/examples/s4_speed_slow.mp3"></audio>\
<br>Fast music<br><audio controls src="resources/examples/s4_speed_fast.mp3"></audio>',

/* LOUDNESS */
'<h1>2. Loudness</h1>This refers to your perception of the music\'s volume (i.e., intensity).\
<br>Your responses can range from: very soft to very loud.\
<br><br>Examples:\
<br>Soft music<br><audio controls src="resources/examples/s3_dynamic_soft.mp3"></audio>\
<br>Loud music<br><audio controls src="resources/examples/s3_dynamic_loud.mp3"></audio>',

/* REGISTER */
'<h1>3. Register</h1>This refers to your perception of the music\'s overall pitch height (i.e., frequency).\
<br>Your responses can range from: very low to very high.\
<br><br>Examples:\
<br>Low music<br><audio controls src="resources/examples/s1_register_low.mp3"></audio>\
<br>High music<br><audio controls src="resources/examples/s1_register_high.mp3"></audio>',

/* ARTICULATION */
'<h1>4. Articulation</h1>This refers to your perception of the music\'s smoothness (musical terms: <i>legato</i>, <i>staccato</i>).\
<br>Your responses can range from: very smooth to very spiky.\
<br><br>Examples:\
<br>Smooth music<br><audio controls src="resources/examples/s1_articulation_smooth.mp3"></audio>\
<br>Spiky music<br><audio controls src="resources/examples/s1_articulation_spiky.mp3"></audio>',

/* TEXTURE */
'<h1>5. Texture</h1>This refers to the music\'s density (i.e., thickness).\
<br>Your responses can range from: very dense to very sparse.\
<br><br>Examples:\
<br>Dense music<br><audio controls src="resources/examples/s7_texture_dense.mp3"></audio>\
<br>Sparse music<br><audio controls src="resources/examples/s7_texture_sparse.mp3"></audio>',

/* SOUND-COLOUR */
'<h1>6. Sound-colour</h1>This refers to the tone quality of the music (i.e., timbre).\
<br>Your responses can range from: very dark to very bright.\
<br><br>Examples:\
<br>Dark music<br><audio controls src="resources/examples/s6_timbre_dark.mp3"></audio>\
<br>Bright music<br><audio controls src="resources/examples/s6_timbre_bright.mp3"></audio>',

'The listening section of the experiment is about to begin.<br><br>\
Your task is to listen to short musical clips and judge the features<br>\
of each piece by selecting from the options provided.<br><br>\
You can also type your own description of each<br>\
clip into a text box.<br><br>\
Please listen carefully to the musical clips and answer the questions<br>\
to the best of your ability. Thank you!',
'When you are ready, click <b>continue</b> and <br>the experiment will begin.'

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
timeline.push(instructions);
