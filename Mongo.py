
import os
from pymongo import MongoClient
import gridfs
import json


def file_exists(filename, folder_path):
    file_path = os.path.join(folder_path, filename)
    return os.path.exists(file_path)


def read_json(file_path):
    with open(file_path, 'r') as file:
        json_data = json.load(file)
    return json_data


wave_dir = "C:/Users/amine/Desktop/watch/"
finger_dir = "C:/Users/amine/Desktop/Fingerprints/"

client = MongoClient('mongodb://localhost:27017/')
db = client['snrt']
collection = db['snrt']
fs = gridfs.GridFS(db)

all_documents = collection.find({})
for document in all_documents:
    x = document['soundfile_name']
    if file_exists(str(x).replace("wav", "json"), wave_dir) and file_exists(str(x).replace("wav", "json"), finger_dir):
        fingerprint_data = read_json(finger_dir + str(x).replace("wav", "json"))
        waveform_data = read_json(wave_dir + str(x).replace("wav", "json"))

        fingerprint_id = fs.put(json.dumps(fingerprint_data).encode('utf-8'))
        waveform_id = fs.put(json.dumps(waveform_data).encode('utf-8'))

        try:

            result = collection.update_one({"soundfile_name": x}, {"$set": {"fingerprint_id": fingerprint_id, "waveform_id": waveform_id}})
            print(f"Updated {result.modified_count} document(s) for soundfile {x}")
        except Exception as e:
            print(f"Error updating document for soundfile {x}: {e}")

