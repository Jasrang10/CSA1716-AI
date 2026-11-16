import tensorflow as tf
from tensorflow.keras import layers, models

(xtr, ytr), (xte, yte) = tf.keras.datasets.mnist.load_data()
xtr, xte = xtr/255.0, xte/255.0

model = models.Sequential([
    layers.Flatten(input_shape=(28,28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(xtr, ytr, epochs=5, validation_split=0.1)
loss, acc = model.evaluate(xte, yte)
print("Test accuracy:", acc)
