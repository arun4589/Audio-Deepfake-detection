import librosa
import numpy as np
import os
from tqdm import tqdm

def load_audio(file_path, sr=16000):
    audio, _ = librosa.load(file_path, sr=sr)
    return audio

def load_dataset(data_dir):
    audio_files = []
    labels = []

    for label in ['genuine', 'spoof']:
        label_dir = os.path.join(data_dir, label)
        for file_name in tqdm(os.listdir(label_dir)):
            file_path = os.path.join(label_dir, file_name)
            audio = load_audio(file_path)
            audio_files.append(audio)
            labels.append(0 if label == 'genuine' else 1)
    
    return np.array(audio_files), np.array(labels)
