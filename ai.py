import connect4
import tensorflow as tf
import numpy as np

ROWS = 6
COLS = 7

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(ROWS, COLS)),
    tf.keras.layers.Dense(50, activation='relu'),
    tf.keras.layers.Dense(COLS, activation='relu')
])

model.summary()
game = connect4.Connect4()

print([game.board])
print(model.predict(game.get_board_for_training(), verbose=1))