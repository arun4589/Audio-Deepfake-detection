import tensorflow as tf
from src.data_loader import load_dataset
from src.model import rawnet2

data_dir = "data/ASVspoof2019_LA"
X, y = load_dataset(data_dir)

model = rawnet2()
model.fit(X, y, batch_size=32, epochs=20, validation_split=0.2)

model.save('results/checkpoints/rawnet2.h5')
print("Training complete. Model saved.")
