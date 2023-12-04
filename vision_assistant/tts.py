"""Function for converting input text into synthesized speech using the current Text-To-Speech Model.
Current TTS model: pyttsx3 (https://pypi.org/project/pyttsx3/)
TODO: checkout Festival Text to Speech, mycroft-AI Mimic3(https://github.com/MycroftAI/plugin-tts-mimic3/blob/67552a4167752caa2998efb75d55e588a81a4d92/mycroft_plugin_tts_mimic3/__init__.py#L170)
"""
import pyttsx3
import requests
from google.cloud import texttospeech
import os


def say(input_text: str) -> None:
    """Check if the device is online or offline, and call appropriate say method."""
    request = requests.get("http://clients3.google.com/generate_204")
    if request.status_code == 204:
        say_online(input_text)
    else:
        say_offline(input_text)


def say_offline(text_input: str) -> None:
    """Read text_input aloud to the user using the current text to speech model.

    Parameters
    ----------
    text_input : str
        The text to be read aloud to the user.

    Returns
    -------
    None
    """

    # instantiate text to speech engine
    tts = pyttsx3.init()

    # set appropriate speech rate for the model
    tts.setProperty("rate", 170)

    # read the input text aloud
    tts.say(text_input)
    tts.runAndWait()


def say_online(input_text: str) -> None:
    # instantiate the google cloud text to speech client
    client = texttospeech.TextToSpeechClient()

    # set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=input_text)

    # configure the voice to be used for synthesis
    voice = texttospeech.VoiceSelectionParams(language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)

    # select type of audio file to be returned
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    # perform text to speech request with the above parameters
    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    # write the response as an mp3 file
    with open("./data/temp/output.mp3", "wb") as output:
        output.write(response.audio_content)
        print("speech generated...")

    # play the generated speech
    os.system("mpg123 ./data/temp/output.mp3")


if __name__ == "__main__":
    say("Hello! I am AI-Reader, and I will be your reading assistant for today.")
