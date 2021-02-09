import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/nelsongou/Desktop/tts-key.json"
from google.cloud import texttospeech

prm_text = "water" # text which the output mp3 will say
prm_voice = "ru-RU-Wavenet-B" # look here: https://cloud.google.com/text-to-speech/docs/voices
prm_speed = 1.0 # speed: 0.25 - 4.0, default = 1.0
prm_pitch = 0.0 # pitch: -20.0 - 20.0, default = 0.0

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
outfile = prm_voice + '.mp3'
with open(outfile, 'wb') as out:
    out.write(response.audio_content) # Write the response to the output file
print('Audio file generated as ' + prm_voice + '.mp3')
