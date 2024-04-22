import queue
import sys
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer

model = Model("model")
samplerate = 16000
device = 1

q = queue.Queue()

def stream_callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def listen_commands(callback):
    with sd.RawInputStream(samplerate=samplerate, blocksize = 8000, device=device,
                            dtype="int16", channels=1, callback=stream_callback):
        rec = KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                callback(json.loads(rec.Result())["text"])