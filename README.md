# Audio File Monitoring and Processing System

## Overview
This project is designed to monitor audio files in a specified directory, process them, and store the processed data in a MongoDB database. It includes functionality to convert WAV files to MP3, generate waveform data, and extract fingerprints from audio files.

## Features
- **Real-time Monitoring**: The system continuously monitors a specified directory for audio file changes using the watchdog library.
- **File Conversion**: Automatically converts WAV files to MP3 format for compatibility.
- **Waveform Data Generation**: Extracts waveform data from audio files using the librosa library and saves it in JSON format.
- **Fingerprint Extraction**: Calculates and stores audio fingerprints in JSON format for each audio file.
- **MongoDB Integration**: Utilizes MongoDB for storing fingerprint and waveform data.
- **Scalability**: Easily scalable to handle large volumes of audio files.

## Installation
1. Clone the repository:
```sh
git clone <repository_url>
```
2. Install the required Python dependencies:
```sh
pip install -r requirements.txt
```
3.Set up MongoDB on your local machine or provide the appropriate MongoDB connection URI in the code.

## Usage
-**Run the main Python script to start monitoring the specified directory:**
```sh
python audio_monitor.py
```
-**Place audio files in the monitored directory to trigger processing.**

## Configuration##
    -Adjust the monitored directory path in the audio_monitor.py script as needed
    -Modify MongoDB connection settings in the utilisateur_services.py script.

## Tech Stack

- **Python**: Main programming language for file monitoring and processing.
- **watchdog**: Library for monitoring file system events.
- **librosa**: Python package for audio and music analysis.
- **pymongo**: Python driver for MongoDB.

## Contributing

  1-Fork the repository.
  2-Create a new branch (git checkout -b feature/my-feature).
  3-Commit your changes (git commit -am 'Add new feature').
  4-Push to the branch (git push origin feature/my-feature).
  5-Create a new Pull Request.
    




