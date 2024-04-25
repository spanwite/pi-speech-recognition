import queue
import sys
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer

vosk_model_ru = Model("vosk_model_ru") # модель для распознавания речи
samplerate = 16000 # частота дискретизации аудио
device = 1 # устройство, для записи звука

q = queue.Queue()

def stream_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def listen_commands(callback):
    with sd.RawInputStream(samplerate=samplerate, blocksize = 8000, device=device,
                            dtype="int16", channels=1, callback=stream_callback):
        rec = KaldiRecognizer(vosk_model_ru, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                callback(json.loads(rec.Result())["text"])