import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/nelsongou/Desktop/tts-key.json"
from google.cloud import texttospeech

prm_text = "food" # text which the output mp3 will say
prm_speed = 1.0 # speed: 0.25 - 4.0, default = 1.0
prm_pitch = 0.0 # pitch: -20.0 - 20.0, default = 0.0


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
    outfile = '/Users/nelsongou/Desktop/Words/' + prm_text + '/' + prm_voice + '.mp3'
    with open(outfile, 'wb') as out:
        out.write(response.audio_content) # Write the response to the output file
    print('Audio file generated as ' + prm_voice + '.mp3')

    return


voices = ['fr-FR-Standard-A',
 'fr-FR-Standard-B',
 'fr-FR-Standard-C',
 'fr-FR-Standard-D',
 'fr-FR-Standard-E',
 'fr-FR-Wavenet-A',
 'fr-FR-Wavenet-B',
 'fr-FR-Wavenet-C',
 'fr-FR-Wavenet-D',
 'fr-FR-Wavenet-E',
 'ja-JP-Standard-A',
 'ja-JP-Standard-B',
 'ja-JP-Standard-C',
 'ja-JP-Standard-D',
 'ja-JP-Wavenet-A',
 'ja-JP-Wavenet-B',
 'ja-JP-Wavenet-C',
 'ja-JP-Wavenet-D',
 'ko-KR-Standard-A',
 'ko-KR-Standard-B',
 'ko-KR-Standard-C',
 'ko-KR-Standard-D',
 'ko-KR-Wavenet-A',
 'ko-KR-Wavenet-B',
 'ko-KR-Wavenet-C',
 'ko-KR-Wavenet-D',
 'ru-RU-Standard-A',
 'ru-RU-Standard-B',
 'ru-RU-Standard-C',
 'ru-RU-Standard-D',
 'ru-RU-Standard-E',
 'ru-RU-Wavenet-A',
 'ru-RU-Wavenet-B',
 'ru-RU-Wavenet-C',
 'ru-RU-Wavenet-D',
 'ru-RU-Wavenet-E',
 'tr-TR-Standard-A',
 'tr-TR-Standard-B',
 'tr-TR-Standard-C',
 'tr-TR-Standard-D',
 'tr-TR-Standard-E',
 'tr-TR-Wavenet-A',
 'tr-TR-Wavenet-B',
 'tr-TR-Wavenet-C',
 'tr-TR-Wavenet-D',
 'tr-TR-Wavenet-E']

voicesRU = ['ru-RU-Standard-A',
 'ru-RU-Standard-B',
 'ru-RU-Standard-C',
 'ru-RU-Standard-D',
 'ru-RU-Standard-E',
 'ru-RU-Wavenet-A',
 'ru-RU-Wavenet-B',
 'ru-RU-Wavenet-C',
 'ru-RU-Wavenet-D',
 'ru-RU-Wavenet-E']

for prm_voice in voicesRU:
    text2speech(prm_text, prm_voice, prm_speed, prm_pitch)

print(len(voicesRU), "audio files have been generated")
