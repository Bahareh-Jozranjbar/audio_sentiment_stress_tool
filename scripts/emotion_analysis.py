from transformers import pipeline

def analyze_emotion(audio_transcription):
    classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
    result = classifier(audio_transcription)
    return result

if __name__ == "__main__":
    transcription = "I love this game, but it's a bit challenging."
    emotions = analyze_emotion(transcription)
    print("Emotion Analysis:", emotions)
