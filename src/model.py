import tensorflow as tf
from tensorflow.keras import layers

def rawnet2(input_shape=(16000,)):
    inputs = tf.keras.Input(shape=input_shape)

    # Convolutional Block
    x = layers.Conv1D(64, kernel_size=3, padding='same', activation='relu')(inputs)
    x = layers.BatchNormalization()(x)
    x = layers.MaxPooling1D(pool_size=2)(x)

    # Residual Block
    for _ in range(3):
        shortcut = x
        x = layers.Conv1D(128, kernel_size=3, padding='same', activation='relu')(x)
        x = layers.BatchNormalization()(x)
        x = layers.Add()([shortcut, x])

    # Global Pooling and Dense Layers
    x = layers.GlobalAveragePooling1D()(x)
    x = layers.Dense(64, activation='relu')(x)
    x = layers.Dense(1, activation='sigmoid')(x)

    model = tf.keras.Model(inputs, x, name='RawNet2')
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model
