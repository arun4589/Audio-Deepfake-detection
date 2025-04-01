
# Audio Deepfake Detection (RawNet2)

This repository contains an implementation of an **Audio Deepfake Detection** system using **RawNet2** architecture, designed to classify AI-generated human speech (deepfakes) and genuine audio. The system is capable of training and evaluating a model on the ASVspoof 2019 dataset (or other suitable datasets), and it is optimized for both training and evaluation of deepfake detection models.

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Dataset](#dataset)
4. [File Structure](#file-structure)
5. [Training](#training)
6. [Evaluation](#evaluation)
7. [Results](#results)


## Introduction

This project aims to detect **AI-generated human speech** (deepfakes) using **RawNet2**, a deep learning model architecture specifically designed for raw waveform speech processing. The model is trained using the ASVspoof 2019 dataset and can be easily adapted to other audio datasets.

The goal is to implement a robust system for detecting spoofed audio and deploying it in real-world applications, such as security systems, voice authentication, and content verification.

## Getting Started

### Prerequisites

1. **Python 3.8+**: Make sure you have Python installed on your machine. You can download it from [here](https://www.python.org/downloads/).
2. **Virtual Environment**: It is recommended to use a virtual environment to manage dependencies.
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
Installation
Clone the repository and install the required dependencies
git clone https://github.com/yourusername/audio-deepfake-detection-rawnet2.git
cd audio-deepfake-detection-rawnet2
pip install -r requirements.txt


## Dataset
The project uses the ASVspoof 2019 dataset for training and evaluation. Follow these steps to download and set up the dataset:
bash data/download_dataset.sh

The dataset will be downloaded and unzipped into the data/ folder.

## File Structure
The repository is organized as follows:
audio-deepfake-detection-rawnet2/

├── README.md                  # Project overview and instructions

├── setup.py                   # Setup script for the project

├── requirements.txt           # Python dependencies

├── data/                      # Dataset folder
│   ├── README.md              # Dataset description and usage
│   └── download_dataset.sh    # Script to download and unzip dataset

├── notebooks/                 # Jupyter notebooks for experimentation
│   ├── data_preprocessing.ipynb  # Data exploration and preprocessing
│   ├── model_training.ipynb    # Model training pipeline
│   └── evaluation.ipynb        # Model evaluation and inference

├── src/                       # Source code for the project
│   ├── __init__.py
│   ├── data_loader.py         # Functions to load and preprocess data
│   ├── model.py               # Model architecture (RawNet2)
│   ├── trainer.py             # Model training script
│   └── evaluate.py            # Model evaluation script

├── scripts/                   # Shell scripts for training and evaluation
│   ├── train.sh               # Shell script to train the model
│   └── evaluate.sh            # Shell script to evaluate the model

└── results/                   # Output folder (logs, checkpoints, reports)
    ├── logs/
    ├── checkpoints/
    └── evaluation_report.txt


## Training
To train the model, run the following command:

bash scripts/train.sh


This will:

Load the dataset from the data/ folder.

Train the RawNet2 model using the ASVspoof 2019 dataset.

Save the model in the results/checkpoints/ directory.

## Evaluation
After training, you can evaluate the model on the test dataset by running:

bash scripts/evaluate.sh
This will:

Load the trained model from the results/checkpoints/ directory.

Evaluate the model on the test set.

Save the evaluation results in results/evaluation_report.txt.

## Results
Evaluation results, including model performance on the test set, are saved in the results/evaluation_report.txt file. You can review the test accuracy, loss, and observations about the model's performance

