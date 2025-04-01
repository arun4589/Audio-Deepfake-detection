
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
