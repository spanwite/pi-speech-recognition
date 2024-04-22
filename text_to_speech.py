import torch
import sounddevice as sd

language = 'ru'
model_id = 'v4_ru'
sample_rate = 48000
speaker = 'aidar'
device = torch.device('cpu')

model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                          model='silero_tts',
                          language=language,
                          speaker=model_id)
model.to(device)

def say_text(text: str):
    print(f'Озвучиваю: "{text}"...')
    audio = model.apply_tts(text=text, speaker=speaker, sample_rate=sample_rate)

    sd.play(audio, sample_rate)