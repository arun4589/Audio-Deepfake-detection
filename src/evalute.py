import tensorflow as tf
from src.data_loader import load_dataset

model = tf.keras.models.load_model('results/checkpoints/rawnet2.h5')
data_dir = "data/ASVspoof2019_LA"
X_test, y_test = load_dataset(data_dir)

results = model.evaluate(X_test, y_test)
print(f"Test Loss: {results[0]}, Test Accuracy: {results[1]}")

with open("results/evaluation_report.txt", "w") as file:
    file.write(f"Test Loss: {results[0]}\n")
    file.write(f"Test Accuracy: {results[1]}\n")
