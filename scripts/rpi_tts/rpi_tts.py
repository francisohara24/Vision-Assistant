"""Test Mozilla-TTS models on Raspberry Pi"""

### RUN THE FOLLOWING COMMANDS IN TERMINAL TO INSTALL REQUIRED LIBRARIES
# cd scripts/rpi_tts
# sudo apt-get install espeak
# clone fork of coqui-ai repository and install required python modules
# git clone https://github.com/francisohara24/TTS.git
# cd TTS
# pip install -r ./requirements.txt
# python setup.py install
# cd ..

### RUN THE FOLLOWING COMMANDS TO DOWNLOAD PRE-TRAINED MODELS
# mkdir models
# gdown --id 12pTojgg7qoXrsnyMsNl-WOil1eetZh7L -O ./models/tts_model.pth.tar
# gdown --id 12Z5r4rdOx_7LmD-pyXvIyt4vvGpCmOQy -O ./models/config.json

# gdown --id 12YvyBhE17VYIjOg4vYWD_xKAAdB0r4qE -O ./models/vocoder_model.pth.tar
# gdown --id 12npX6u1RbMZzV6LBlnKQcazZbwfFTQlk -O ./models/config_vocoder.json
# gdown --id 12oeQ3slzyr4lyMEfs-OfV_RUiJg8cOz7 -O ./models/scale_stats.npy


# Define TTS function
def tts(model, text, CONFIG, use_cuda, ap, use_gl, figures=True):
    t_1 = time.time()
    waveform, alignment, mel_spec, mel_postnet_spec, stop_tokens, inputs = synthesis(model, text, CONFIG, use_cuda, ap, speaker_id, style_wav=None, truncated=False, enable_eos_bos_chars=CONFIG.enable_eos_bos_chars)

    # mel_postnet_spec = ap._denormalize(mel_postnet_spec.T)
    if not use_gl:
        waveform = vocoder_model.inference(torch.FloatTensor(mel_postnet_spec.T).unsqueeze(0))
        waveform = waveform.flatten()
    if use_cuda:
        waveform = waveform.cpu()

    waveform = waveform.numpy()

    rtf = (time.time() - t_1) / (len(waveform) / ap.sample_rate)
    tps = (time.time() - t_1) / len(waveform)
    print(waveform.shape)
    print(" > Run-time: {}".format(time.time() - t_1))
    print(" > Real-time factor: {}".format(rtf))
    print(" > Time per step: {}".format(tps))
# TODO: determine duration of resulting wav file and call time.sleep for that duration.
    sd.play(waveform, ap.sample_rate)
    time.sleep(120)
    sd.stop()
    return alignment, mel_postnet_spec, stop_tokens, waveform

# Load Models
import os
import torch
import time
import sounddevice as sd

from TTS.utils.generic_utils import setup_model
from TTS.utils.io import load_config
from TTS.utils.text.symbols import symbols, phonemes
from TTS.utils.audio import AudioProcessor
from TTS.utils.synthesis import synthesis

# runtime settings
use_cuda = False

# model paths
TTS_MODEL = "./models/tts_model.pth.tar"
TTS_CONFIG = "./models/config.json"
VOCODER_MODEL = "./models/vocoder_model.pth.tar"
VOCODER_CONFIG = "./models/config_vocoder.json"

# load configs
TTS_CONFIG = load_config(TTS_CONFIG)
VOCODER_CONFIG = load_config(VOCODER_CONFIG)

# load the audio processor
ap = AudioProcessor(**TTS_CONFIG.audio)

# LOAD TTS MODEL
# multi speaker
speaker_id = None
speakers = []

# load the model
num_chars = len(phonemes) if TTS_CONFIG.use_phonemes else len(symbols)
model = setup_model(num_chars, len(speakers), TTS_CONFIG)

# load model state
cp =  torch.load(TTS_MODEL, map_location=torch.device('cpu'))

# load the model
model.load_state_dict(cp['model'])
if use_cuda:
    model.cuda()
model.eval()

# set model stepsize
if 'r' in cp:
    model.decoder.set_r(cp['r'])

from TTS.vocoder.utils.generic_utils import setup_generator

# LOAD VOCODER MODEL
vocoder_model = setup_generator(VOCODER_CONFIG)
vocoder_model.load_state_dict(torch.load(VOCODER_MODEL, map_location="cpu")["model"])
vocoder_model.remove_weight_norm()
vocoder_model.inference_padding = 0

ap_vocoder = AudioProcessor(**VOCODER_CONFIG['audio'])
if use_cuda:
    vocoder_model.cuda()
vocoder_model.eval()

# Run Inference
sentence = open("./data/colby_affirmation.txt").read()
align, spec, stop_tokens, wav = tts(model, sentence, TTS_CONFIG, use_cuda, ap, use_gl=False, figures=True)
