# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# File:             tts-batch.py
# Description:      Generates mp3 files using various voices from the Google Text-to-Speech API
# Author:           Nelson Gou, Eric Zhang
# Creation Date:    1/18/2021
#
# Copyright © 2020-2021 Nelson Gou, Eric Zhang. All rights reserved.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/nelsongou/Desktop/tts-key.json"
from google.cloud import texttospeech

prm_text = "food" # text which the output mp3 will say
prm_speed = 1.0 # speed: 0.25 - 4.0, default = 1.0

def text2speech(prm_text, prm_voice, prm_speed, prm_pitch):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(
        text=prm_text)

    # Build the voice request
    voice = texttospeech.VoiceSelectionParams(
    name=prm_voice, 
    language_code=prm_voice[:prm_voice.find('-', prm_voice.find('-')+1)], 
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3,
    speaking_rate=prm_speed, 
    pitch=prm_pitch 
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # The response's audio_content is binary.
    outfile = '/Users/nelsongou/Desktop/Words/' + prm_text + '/' + prm_voice + '_' + str(prm_pitch) + '.mp3'
    with open(outfile, 'wb') as out:
        out.write(response.audio_content) # Write the response to the output file
    print('Audio file generated as ' + prm_voice + '_' + str(prm_pitch) + '.mp3')

    return


voices = ['es-ES-Standard-A',
 'es-ES-Standard-B',
 'es-ES-Wavenet-B',
 'fr-FR-Standard-A',
 'fr-FR-Standard-B',
 'fr-FR-Standard-C',
 'fr-FR-Standard-D',
 'fr-FR-Standard-E',
 'fr-FR-Wavenet-A',
 'fr-FR-Wavenet-B',
 'fr-FR-Wavenet-C',
 'fr-FR-Wavenet-D',
 'fr-FR-Wavenet-E',
 'pt-PT-Standard-A',
 'pt-PT-Standard-B',
 'pt-PT-Standard-C',
 'pt-PT-Standard-D',
 'pt-PT-Wavenet-A',
 'pt-PT-Wavenet-B',
 'pt-PT-Wavenet-C',
 'pt-PT-Wavenet-D',]

pitches = [-3.0, 0.0, 3.0]

for prm_voice in voices:
    for prm_pitch in pitches:
        text2speech(prm_text, prm_voice, prm_speed, prm_pitch)

print((len(voices)*len(pitches)), "audio files have been generated")
