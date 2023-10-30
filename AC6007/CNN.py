# /Users/jiananwang/pycharm_projects/AC6007WEEK11/bin python3
# -*- coding: utf-8 -*-
# week 11 CNN

import random
import pandas as pd
import numpy as np
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Dropout, Flatten, Dense
import scipy
import matplotlib.pyplot as plt

print("---")
random.seed(1)
np.random.seed(1)
tf.random.set_seed(1)
print("---")

# set the dir
train_dir = "data/chest_xray/train"
test_dir = "data/chest_xray/test"

# set train set and test set
train_data = ImageDataGenerator().flow_from_directory(train_dir, (150,150), batch_size=5, shuffle=False)
test_data = ImageDataGenerator().flow_from_directory(test_dir, (150,150), batch_size=5, shuffle=False)

# first layer
model = Sequential()
model.add(Conv2D(32, (3,3), input_shape=(150,150,3), activation="relu"))
model.add(MaxPool2D(pool_size=(2,2), strides=2))
model.add(Dropout(0.1))

# second layer
model.add(Conv2D(32, (3,3), activation="relu"))
model.add(MaxPool2D(pool_size=(2,2), strides=2))
model.add(Dropout(0.1))

# third layer
model.add(Conv2D(64, (3,3), activation="relu"))
model.add(MaxPool2D(pool_size=(2,2), strides=2))
model.add(Dropout(0.1))

# fourth layer
model.add(Conv2D(64, (3,3), activation="relu"))
model.add(MaxPool2D(pool_size=(2,2), strides=2))
model.add(Dropout(0.1))

#
model.add(Flatten())
model.summary

#
model.add(Dense(123, activation='relu'))
model.add(Dropout(0.1))

# output layer
# take the weighted average of the two neural network
model.add(Dense(2, activation='softmax'))

#
model.compile(loss="categorical_crossentropy", optimizer="adam",metrics=["accuracy"])

# train the model
h = model.fit(train_data, batch_size=5, epochs=1)

# plot
plt.plot(h.history['loss'])

# predict
print(model.evaluate(test_data))
