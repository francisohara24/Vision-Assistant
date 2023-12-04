"""Function for converting input text into synthesized speech using the current Text-To-Speech Model.
Offline TTS model: pyttsx3 (https://pypi.org/project/pyttsx3/)
Online TTS model: Google Cloud Text-to-Speech API
"""
# import required libraries
import pyttsx3
import requests
from google.cloud import texttospeech
import os


# function for synthesizing speech from text
def say(input_text: str) -> None:
    """Check if the device is online or offline, and call appropriate speech synthesis method."""
    request = requests.get("http://clients3.google.com/generate_204")
    if request.status_code == 204:
        say_online(input_text)
    else:
        say_offline(input_text)


def say_offline(input_text: str) -> None:
    """Read `input_text` aloud to the user using the offline text to speech model.

    Parameters
    ----------
    input_text : str
        The text to be read aloud to the user.

    Returns
    -------
    None
    """

    # instantiate offline text to speech engine
    tts = pyttsx3.init()

    # set appropriate speech rate for the model
    tts.setProperty("rate", 170)

    # read the input text aloud
    tts.say(input_text)
    tts.runAndWait()


def say_online(input_text: str) -> None:
    """Read the string `text_input` aloud to the user using the online text to speech model.

    Parameters
    ----------
    input_text : str
        The text to be read aloud to the user.

    Returns
    -------
    None
    """
    # instantiate the google cloud text to speech client
    client = texttospeech.TextToSpeechClient()

    # set the input_text to be synthesized by the model
    synthesis_input = texttospeech.SynthesisInput(text=input_text)

    # configure the voice to be used for synthesis
    voice = texttospeech.VoiceSelectionParams(language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)

    # select appropriate audio format for the synthesized speech (mp3)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    # perform text to speech request with the above options
    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    # write the response into an mp3 file
    with open("~/Projects/Vision-Assistant/data/temp/output.mp3", "wb") as output:
        output.write(response.audio_content)
        print("speech generated...")  # print message to aid in remote debugging

    # play the generated speech using system command
    os.system("mpg123 ./data/temp/output.mp3")


# main script for testing the module
if __name__ == "__main__":
    say("Hello! I am Vision-Assistant, and I will be your reading assistant for today.")
