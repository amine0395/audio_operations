import librosa
import librosa.display
import numpy as np
import json


def waveform(wav_file):
    output_file = str(wav_file.replace(".wav", ".json")).replace("C:/Users/amine/Desktop/watch/",
                                                                "C:/Users/amine/Desktop/Wave/")
    y, sr = librosa.load(wav_file)
    time = np.arange(0, len(y)) / sr
    data = {"time": time.tolist(), "amplitude": y.tolist(), "sample_rate": sr}
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file)
