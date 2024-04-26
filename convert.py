from pydub import AudioSegment
import os

def wav_to_mp3(input_wav_file):
    try:
        audio = AudioSegment.from_wav(input_wav_file)
        output_dir = "C:/Users/amine/Desktop/Lake/"
        file_name = os.path.basename(input_wav_file)
        output_mp3_file = os.path.join(output_dir, os.path.splitext(file_name)[0] + ".mp3")
        audio.export(output_mp3_file, format="mp3", bitrate="128k")
        return output_mp3_file
    except Exception as e:
        print(f"Error : {e}")
        return None
