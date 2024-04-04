import queue
import sys
import sounddevice as sd

from vosk import Model, KaldiRecognizer

model = Model("model")
samplerate = 16000
device = 1

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

try:
    with sd.RawInputStream(samplerate=samplerate, blocksize = 8000, device=device,
                           dtype="int16", channels=1, callback=callback):
        rec = KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                print(rec.Result())
except KeyboardInterrupt:
    print("\nDone")