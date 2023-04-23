import tensorflow as tf
from tensorflow import keras
import numpy
import matplotlib.pyplot as pylt
from time import time
import torch
from torch import nn, optim
from torchvision import transforms as tr
from torchvision import utils
from keras.utils import np_utils
from keras import backend as K
K.set_image_dim_ordering('th')
# Imports modules. Are all of these needed ? Most of these do not appear to be used.


(x_train, y_train) , (x_test, y_test) = tf.keras.datasets.mnist.load_data()
print(y_train[13])
# Loads the mnist dataset and splits it into training and testing data. x corresponds to the hand drawn digit and y to the digit label captions

x_train = x_train.reshape(x_train.shape[0], 1, 28, 28).astype('float32')
x_test = x_test.reshape(x_test.shape[0], 1, 28, 28).astype('float32')
# Reshapes images to be in 4 dimensions, converts images to floats that use 32 bits using keras

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)
# Normalises the images from pixel values 0-255 to 0-1 using keras

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
# Categories the digit labels

sequen = tf.keras.models.Sequential()
# Loads the sequential model function to build the neural network
sequen.add(tf.keras.layers.Conv2D(24, (5,5), input_shape=(1, 28, 28), activation='relu',data_format='channels_first'))
sequen.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
sequen.add(tf.keras.layers.Conv2D(15, (3, 3), activation='relu'))
sequen.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
# Adds two convolutional layers to the network. Adds two MaxPooling layers to shrink the image data twice.
sequen.add(tf.keras.layers.Dropout(0.2))
sequen.add(tf.keras.layers.Flatten())
# Adds a dropout and flattern layer to convert the 2D arrays to 1D arrays
sequen.add(tf.keras.layers.Dense(128, activation="relu"))
sequen.add(tf.keras.layers.Dense(50, activation="relu"))
sequen.add(tf.keras.layers.Dense(10, activation='softmax'))
# Adds 3 dense layers to the model. The first two use the relu activation function as they are hidden layers.
# The last uses 10 neurons, one for each digit and the softmax activation function to return a probability between 0 and 1
sequen.compile(optimizer="adam",loss='categorical_crossentropy',metrics=["accuracy"])
# Compiles the model

sequen.fit(x=x_train, y=y_train, epochs=10)
# Fits the training data to the model and sets it to run over 10 epochs to train the data
sequen.save("readnum.sequen")
# Saves the trained model


newsequen = tf.keras.models.load_model("readnum.sequen")
# loads the saved model

pred = newsequen.predict([x_train])
print(numpy.argmax(pred[13]))
pred.im

# Used for testing the predictions of the saved model.








