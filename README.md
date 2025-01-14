# Audio Sentiment and Emotion Analysis Tool

This project analyzes audio files to detect emotions and sentiment, making it particularly useful for UX researchers to understand user feedback in scenarios like game testing. The tool extracts audio features, performs sentiment/emotion analysis, and visualizes results.


## Project Structure
```
AUDIO_SENTIMENT_STRESS_TOOL/
├── audio_samples/
│   └── tester1.mp3          # User-provided audio file for analysis
├── data/
│   ├── waveform_tester1.png # Waveform visualization of the audio
├── scripts/
│   ├── preprocess_audio.py  # Script to preprocess audio and generate waveforms
│   ├── extract_features.py  # Script to extract audio features (MFCC, RMS, pitch)
│   ├── emotion_analysis.py  # Script to analyze emotions from audio features
│   └── visualize_results.py # Script to visualize results (optional)
└── README.md                # Project description and instructions
```



## Features

1. **Audio Preprocessing**:
   - Converts audio to a visual waveform for quick review.
2. **Feature Extraction**:
   - Extracts key audio features such as MFCCs, RMS energy, and pitch.
3. **Emotion Analysis**:
   - Uses a pre-trained deep learning model to classify emotions (Joy, Anger, Sadness).
4. **Visualization**:
   - Displays emotion scores in a clear and interpretable bar chart.

---

## Installation

### Prerequisites

- Python 3.8 or later
- Virtual Environment

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/audio_sentiment_stress_tool.git
    cd audio_sentiment_stress_tool
    ```

2. Create and activate a virtual environment:

    ```bash
    # Linux/Mac
    python3 -m venv env
    source env/bin/activate

    # Windows
    python -m venv env
    .\env\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Add your audio file:
    - Record or obtain an `.mp3` file of someone speaking (e.g., testing a product or playing a game).
    - Save this file in the `data/` directory.
    - Ensure the file name is `tester1.mp3` or modify the script paths accordingly.


---

## Running the Project

### 1. Preprocess Audio

Generate a waveform for the audio file:

```bash
python scripts/preprocess_audio.py
```

This script will:
Load the audio file (tester1.mp3).
Generate a waveform saved as waveform_tester1.png in the data/ folder.

### 2. Extract Audio Features
Extract key audio features such as MFCC, RMS energy, and pitch:

```bash
python scripts/extract_features.py
```
This script will:
Load the audio file.
Extract features and save them as a JSON file in the data/ folder.

### 3. Analyze Emotions
Perform emotion analysis on the extracted features and visualize the results:

```bash
python scripts/emotion_analysis.py
```

This script will:
Analyze the audio features using the pre-trained model.
Generate a bar chart showing emotion scores (e.g., Joy, Anger, Sadness).

## Example Output

### Emotion Scores for `tester1.mp3`:

| Emotion | Score |
|---------|-------|
| Joy     | 0.85  |
| Anger   | 0.05  |
| Sadness | 0.10  |

---


## License

This project is licensed under the MIT License. Feel free to use, share, and modify it as needed.
