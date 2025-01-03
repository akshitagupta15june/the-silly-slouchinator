answers = ["Yes", "No"]
def playBuzzer():
    music.play_tone(Note.C, music.beat(BeatFraction.WHOLE))
def playGoodMelody():
    music.play_tone(247, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(370, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.DOUBLE))
    music.play_tone(494, music.beat(BeatFraction.WHOLE))
    music.play_tone(440, music.beat(BeatFraction.DOUBLE))
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
    music.play_tone(370, music.beat(BeatFraction.DOUBLE))
    music.play_tone(370, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(370, music.beat(BeatFraction.WHOLE))
    music.play_tone(311, music.beat(BeatFraction.WHOLE))
    music.play_tone(311, music.beat(BeatFraction.WHOLE))
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
    music.play_tone(247, music.beat(BeatFraction.DOUBLE))
    music.play_tone(247, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))
    music.play_tone(370, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.DOUBLE))
    music.play_tone(494, music.beat(BeatFraction.WHOLE))
    music.play_tone(587, music.beat(BeatFraction.DOUBLE))
    music.play_tone(554, music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.DOUBLE))
    music.play_tone(415, music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    music.play_tone(523, music.beat(BeatFraction.HALF))
    music.play_tone(494, music.beat(BeatFraction.HALF))
    music.play_tone(466, music.beat(BeatFraction.WHOLE))
    music.play_tone(233, music.beat(BeatFraction.DOUBLE))
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.DOUBLE))
def showRandomPattern():
    patterns = [images.create_image(". . . . . . # . # . . . . . . # . . . # . # # # ."),
        images.create_image(". # . # . # . . . # # . . . # . # . # . . . # . ."),
        images.create_image(". # # # . # . . . # # . . . # # . . . # . # # # ."),
        images.create_image(". . . . . . # . # . . . . . . # # # # # . . . . .")]
    pattern = patterns[Math.floor(Math.random() * len(patterns))]
    pattern.show_image(0)
def checkPosture():
    
    def on_forever():
        pitch = input.rotation(Rotation.PITCH)
        if pitch > 120 or pitch < 60:
            # Adjusted threshold for neck posture
            playBuzzer()
            basic.show_icon(IconNames.SAD)
        else:
            basic.show_icon(IconNames.HAPPY)
    basic.forever(on_forever)
    
def breakReminder():
    
    def on_forever2():
        basic.pause(180000)
        # 3 minutes
        basic.show_string("Break!")
        playGoodMelody()
        basic.show_icon(IconNames.HAPPY)
        music.play_melody("C5 B A G F E D C ", 120)
    basic.forever(on_forever2)
    
def yesNoRandomQuestion():
    # 3 seconds pause
    
    def on_gesture_shake():
        answer = answers[Math.floor(Math.random() * len(answers))]
        basic.show_string(answer)
        playGoodMelody()
        basic.pause(1000)
    input.on_gesture(Gesture.SHAKE, on_gesture_shake)
    

def on_button_pressed_a():
    playBuzzer()
    showRandomPattern()
input.on_button_pressed(Button.A, on_button_pressed_a)

checkPosture()
breakReminder()
yesNoRandomQuestion()
