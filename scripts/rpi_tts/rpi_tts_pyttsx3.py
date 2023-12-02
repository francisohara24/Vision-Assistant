import pyttsx3

# initialize the text to speech engine
engine = pyttsx3.init()

# set the speech rate to a slower rate than the default
engine.setProperty("rate", 170)

# get all available voices for TTS
voices = engine.getProperty("voices")

# set voice for TTS
engine.setProperty("voices", voices[0].id)

# set input text to be converted
input_text = "Hello World! This is a text to speech model running on the Raspberry Pi 4!"

# convert input text to speech format and play aloud
engine.say(input_text)
engine.runAndWait()

for voice in voices: print(voice.id)