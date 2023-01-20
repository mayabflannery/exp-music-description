/* ----- PreloadAudio Audio ----- */
var audioFiles = [
/* =====================  List all stimuli here  ========================== */
"resources/music/yes-tobeover.mp3",
"resources/music/yes-relayer.mp3",
"resources/music/systemofadown-atwa.mp3",
"resources/music/snarkypuppy-whataboutme.mp3",
"resources/music/sapnajahan-nigam,mohan.mp3",
"resources/music/rone-origami2.mp3",
"resources/music/rone-origami1.mp3",
"resources/music/rone-byebyemacadam2.mp3",
"resources/music/rone-byebyemacadam1.mp3",
"resources/music/robertmiles-children2.mp3",
"resources/music/robertmiles-children1.mp3",
"resources/music/pacificaquartet-bartokstringquartetno4.mp3",
"resources/music/opeth-prologueaprilethereal.mp3",
"resources/music/mcbaise-waterslide2.mp3",
"resources/music/mcbaise-waterslide1.mp3",
"resources/music/lorn-acidrain2.mp3",
"resources/music/lorn-acidrain1.mp3",
"resources/music/lordhuron-thenightwemet.mp3",
"resources/music/ladygaga-alejandro.mp3",
"resources/music/jheneaiko-theworst.mp3",
"resources/music/jacopastorius-fullalbum3.mp3",
"resources/music/jacopastorius-fullalbum2.mp3",
"resources/music/jacopastorius-fullalbum1.mp3",
"resources/music/interstellar-cornfieldchase2.mp3",
"resources/music/interstellar-cornfieldchase1.mp3",
"resources/music/inflames-theend.mp3",
"resources/music/inflames-moonshield.mp3",
"resources/music/icedearth-thephantomoperaghost2.mp3",
"resources/music/icedearth-thephantomoperaghost1.mp3",
"resources/music/grandson-bloodwater.mp3",
"resources/music/frozencrown-battlesinthenight.mp3",
"resources/music/eriknielsen-sketchesiiistaccato.mp3",
"resources/music/epiclowbrass-therainsofcastameregot.mp3",
"resources/music/dunwichbeach-autumn.mp3",
"resources/music/cannons-hurricane.mp3",
"resources/music/cannons-baddream.mp3",
"resources/music/brianeno-thursdayafternoon.mp3",
"resources/music/blur-fortomorrow.mp3",
"resources/music/billieeilish-badguy.mp3",
"resources/music/bach-organsonatano4.mp3",
"resources/music/arianagrande-positions.mp3",
"resources/music/apocalyptica-path.mp3",
"resources/music/agartumsaathho-yagnikandsingh.mp3",
"resources/music/abhimujhmeinkahin-sonunigam.mp3",
/* ========================  End stimuli list  ============================ */
];

var current_stimulus = null;
var replays = 0;

/*  PreloadAudio audio files  */
var preloadAudio = {
    type: jsPsychPreload,
    audio: audioFiles,
    show_progress_bar: true,
    message: "Please wait for the experiment to load.",
    error_message: "The experiment failed to load!",
    max_load_time: 10000,
    show_detailed_errors: true,
};
/* Add preloadAudio to -beginning- of timeline with unshift */
timeline.unshift(preloadAudio);

/* ----- Audio trials ----- */
var stimuli_list = []
for (i in audioFiles) {
	stimuli_list.push({
		stimulus: audioFiles[i],
	})
}

/* This is displayed before the stimulus plays */
var pretest = {
	type: jsPsychHtmlKeyboardResponse,
	stimulus: '<div style="font-size:50px;">Please listen carefully.</div>',
	choices: "NO_KEYS",
/* ===========  Set trial_duration equal to stimulus length (ms) ========== */
	trial_duration: 2000, //async function () {
        //audioLength = await jsPsych.pluginAPI.getAudioBuffer(jsPsych.timelineVariable('stimulus'))
        //       .then((buffer) => {
        //           al = (buffer['duration'] - 2) * 1000;
        //           console.log("Audio length", al, "ms");
        //           return al;
        //       });
        //return audioLength;
    //},
	on_load: function () {
        replays = 0;
        current_stimulus = jsPsych.timelineVariable('stimulus');
		console.log("The current stimulus is: ", current_stimulus);
		context = jsPsych.pluginAPI.audioContext();
		jsPsych.pluginAPI.getAudioBuffer(current_stimulus)
		.then(function(buffer){
			audio = context.createBufferSource();
			audio.buffer = buffer;
			audio.connect(context.destination);
			audio.start(context.currentTime);
		})
		.catch(function(err){
			console.error('Audio file failed to load');
		})
	},
};


likert_labels = ["1", "2", "3", "4", "5"];

function replayStimulus (stim) {
    console.log("Replaying", stim);
    audio.stop();
	jsPsych.pluginAPI.getAudioBuffer(stim)
	.then(function(buffer){
		audio = context.createBufferSource();
		audio.buffer = buffer;
		audio.connect(context.destination);
		audio.start(context.currentTime);
        replays++;
	})
	.catch(function(err){
		console.error('Audio file failed to load');
	})
}

/* Play the stimulus and prompt for response */
/*add progress bar*/
var test = {
	type: jsPsychSurvey,
	title: "Please rate the musical clip by selecting from the options below.",
    pages: [
		[{
            name: "replay",
            type: "html",
            prompt: "Note: you may select more than one response.<br>\
                    Click here to see the <a href='resources/text/terms.html' target='_blank'>musical term definitions</a>\
                    (they will open in a new tab).<br><br>\
                    <button onclick='replayStimulus(current_stimulus)'>Replay the clip</button><br>"

        },
         {
			name: "rate_tempo",
			type: "multi-select",
			prompt: "The speed is:",
			options: ["Very slow", "Slow", "Medium", "Fast", "Very fast"],
            columns: 5,
			required: true,
		},
		{
			name: "rate_dynamic",
			type: "multi-select",
			prompt: "The loudness is:",
			options: ["Very soft", "Soft", "Medium", "Loud", "Very loud"],
            columns: 5,
			required: true,
		},
		{
			name: "rate_register",
			type: "multi-select",
			prompt: "The register is:",
			options: ["Very low", "Low", "Medium", "High", "Very high"],
            columns: 5,
			required: true,
		},
		{
			name: "rate_articulation",
			type: "multi-select",
			prompt: "The articulation is:",
			options: ["Very smooth", "Smooth", "Medium", "Spiky", "Very spiky"],
            columns: 5,
			required: true,
		},
		{
			name: "rate_texture",
			type: "multi-select",
			prompt: "The texture is:",
			options: ["Very dense", "Dense", "Medium", "Sparse", "Very sparse"],
            columns: 5,
			required: true,
		},
		{
			name: "rate_timbre",
			type: "multi-select",
			prompt: "The sound-colour is:",
			options: ["Very dark", "Dark", "Medium", "Bright", "Very bright"],
            columns: 5,
			required: true,
		},
       	{
			name: `described`,
			type: `text`,
			prompt: `How else might you describe the music? (optional)`,
			placeholder: `Type descriptive words here`,
			textbox_columns: 50,
			textbox_rows: 1,
			required: false
		},
        {
            name: "space",
            type: "html",
            prompt: "<br>"

        }]
	],
	button_label_finish: 'Continue',
	show_question_numbers: 'onPage',
	required_error: "Please provide an answer to this question.",
	data: {
		sound: jsPsych.timelineVariable('stimulus'),
	},
    on_finish: function () {
        // Add number of replays to data
        jsPsych.data.write({"replays": replays})
        overall_trial++;
        jsPsych.setProgressBar(overall_trial / all_trials);
    }
};


/* Combine pretest and test */
var test_procedure = {
	timeline: [pretest, test],
	timeline_variables: stimuli_list,
	repetitions: 1,
	randomize_order: true
};
all_trials += audioFiles.length;
timeline.push(test_procedure);
