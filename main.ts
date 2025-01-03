let answers = ["Yes", "No"];

function playBuzzer() {
    music.playTone(Note.C, music.beat(BeatFraction.Whole));
}

function playGoodMelody() {
    music.playTone(247, music.beat(BeatFraction.Whole));
    music.playTone(330, music.beat(BeatFraction.Whole));
    music.playTone(330, music.beat(BeatFraction.Half));
    music.playTone(392, music.beat(BeatFraction.Half));
    music.playTone(370, music.beat(BeatFraction.Whole));
    music.playTone(330, music.beat(BeatFraction.Double));
    music.playTone(494, music.beat(BeatFraction.Whole));
    music.playTone(440, music.beat(BeatFraction.Double));
    music.playTone(440, music.beat(BeatFraction.Whole));
    music.playTone(370, music.beat(BeatFraction.Double));
    music.playTone(370, music.beat(BeatFraction.Whole));
    music.playTone(330, music.beat(BeatFraction.Whole));
    music.playTone(330, music.beat(BeatFraction.Half));
    music.playTone(392, music.beat(BeatFraction.Half));
    music.playTone(370, music.beat(BeatFraction.Whole));
    music.playTone(311, music.beat(BeatFraction.Whole));
    music.playTone(311, music.beat(BeatFraction.Whole));
    music.playTone(349, music.beat(BeatFraction.Whole));
    music.playTone(247, music.beat(BeatFraction.Double));
    music.playTone(247, music.beat(BeatFraction.Whole));
    music.playTone(330, music.beat(BeatFraction.Whole));
    music.playTone(330, music.beat(BeatFraction.Half));
    music.playTone(392, music.beat(BeatFraction.Half));
    music.playTone(370, music.beat(BeatFraction.Whole));
    music.playTone(330, music.beat(BeatFraction.Double));
    music.playTone(494, music.beat(BeatFraction.Whole));
    music.playTone(587, music.beat(BeatFraction.Double));
    music.playTone(554, music.beat(BeatFraction.Whole));
    music.playTone(523, music.beat(BeatFraction.Double));
    music.playTone(415, music.beat(BeatFraction.Whole));
    music.playTone(523, music.beat(BeatFraction.Whole));
    music.playTone(523, music.beat(BeatFraction.Half));
    music.playTone(494, music.beat(BeatFraction.Half));
    music.playTone(466, music.beat(BeatFraction.Whole));
    music.playTone(233, music.beat(BeatFraction.Double));
    music.playTone(392, music.beat(BeatFraction.Whole));
    music.playTone(330, music.beat(BeatFraction.Double));

}

function showRandomPattern() {
    let patterns = [
        images.createImage(". . . . . . # . # . . . . . . # . . . # . # # # ."),
        images.createImage(". # . # . # . . . # # . . . # . # . # . . . # . ."),
        images.createImage(". # # # . # . . . # # . . . # # . . . # . # # # ."),
        images.createImage(". . . . . . # . # . . . . . . # # # # # . . . . .")
    ];
    let pattern = patterns[Math.floor(Math.random() * patterns.length)];
    pattern.showImage(0);
}

function checkPosture() {
    basic.forever(function () {
        let pitch = input.rotation(Rotation.Pitch);
        if (pitch > 120 || pitch < 60) { // Adjusted threshold for neck posture
            playBuzzer();
            basic.showIcon(IconNames.Sad);
        } else {
            basic.showIcon(IconNames.Happy);
        }
    });
}

function breakReminder() {
    basic.forever(function () {
        basic.pause(180000); // 3 minutes
        basic.showString("Break!");
        playGoodMelody();
        basic.showIcon(IconNames.Happy);
        music.playMelody("C5 B A G F E D C ", 120);
    });
}

function yesNoRandomQuestion() {
    input.onGesture(Gesture.Shake, function () {
        let answer = answers[Math.floor(Math.random() * answers.length)];
        basic.showString(answer);
        playGoodMelody();
        basic.pause(1000); // 3 seconds pause
    });
}

input.onButtonPressed(Button.A, function () {
    playBuzzer();
    showRandomPattern();
});

checkPosture();
breakReminder();
yesNoRandomQuestion();