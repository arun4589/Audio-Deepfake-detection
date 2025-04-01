#!/bin/bash
echo "Downloading ASVspoof 2019 dataset..."
wget -P data/ https://zenodo.org/record/2674193/files/ASVspoof2019_LA.zip
unzip data/ASVspoof2019_LA.zip -d data/
rm data/ASVspoof2019_LA.zip
echo "Dataset downloaded and extracted successfully!"