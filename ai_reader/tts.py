"""Function for converting input text into synthesized speech using the current Text-To-Speech Model.
Current TTS model: pyttsx3
"""
import pyttsx3


def say(text_input: str) -> None:
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
    tts.setProperty("rate", 180)

    # read the input text aloud
    tts.say(text_input)
    tts.runAndWait()

if __name__ == "__main__":
    say("Hello! I am AI-Reader, and I will be your reading assistant for today.")