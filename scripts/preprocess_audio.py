import librosa
import librosa.display
import matplotlib.pyplot as plt
import os

def load_audio(file_path, sr=16000):
    audio, sample_rate = librosa.load(file_path, sr=sr)
    return audio, sample_rate

def save_waveplot(audio, sample_rate, output_path):
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(audio, sr=sample_rate)
    plt.title("Waveform")
    plt.savefig(output_path)
    plt.close()
    print(f"Waveform saved to {output_path}")

if __name__ == "__main__":
    file_path = r"C:\Users\mojda\OneDrive\Desktop\data science learning\audio_sentiment_stress_tool\data\tester1.mp3"
    audio, sr = load_audio(file_path)
    save_waveplot(audio, sr, r"data/waveform_tester1.png")
