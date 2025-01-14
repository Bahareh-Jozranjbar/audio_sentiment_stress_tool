import matplotlib.pyplot as plt

def plot_emotions(emotions):
    labels = [e["label"] for e in emotions]
    scores = [e["score"] for e in emotions]

    plt.bar(labels, scores, color="skyblue")
    plt.title("Emotion Scores for tester1.mp3")
    plt.ylabel("Score")
    plt.show()

if __name__ == "__main__":
    emotions = [
        {"label": "joy", "score": 0.85},
        {"label": "anger", "score": 0.05},
        {"label": "sadness", "score": 0.1}
    ]
    plot_emotions(emotions)
