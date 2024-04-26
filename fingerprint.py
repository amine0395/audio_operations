import json
import librosa

def fingerprints(wav_file):

    y, sr = librosa.load(wav_file)

    mel_spectrogram = librosa.feature.melspectrogram(y=y, sr=sr)

    json_fingerprints = []
    for i in range(mel_spectrogram.shape[1]):
        json_fp = {
            "time": i,
            "features": mel_spectrogram[:, i].tolist()
        }
        json_fingerprints.append(json_fp)

    # Save as JSON
    output_file = str(wav_file.replace(".wav", ".json")).replace("C:/Users/amine/Desktop/watch/",
                                                                  "C:/Users/amine/Desktop/Fingerprints/")
    with open(output_file, 'w') as json_file:
        json.dump(json_fingerprints, json_file)


