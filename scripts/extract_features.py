import librosa
import numpy as np
import os

def extract_features(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    # Load the audio file
    print("Loading audio file...")
    audio, sr = librosa.load(file_path, sr=None)

    # Extract features
    print("Extracting features...")
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
    rms = librosa.feature.rms(y=audio)
    pitch, _ = librosa.piptrack(y=audio, sr=sr)

    return {
        "mfccs": mfccs,
        "rms": rms,
        "pitch": pitch
    }

if __name__ == "__main__":
    file_path = "data/tester1.mp3"  # Corrected path
    try:
        features = extract_features(file_path)
        print("Features extracted successfully!")
        print("Feature keys:", features.keys())
    except Exception as e:
        print(f"Error: {e}")
