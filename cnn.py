# -*- coding: utf-8 -*-
"""CNN

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JJ4s6ZwhRer1pe0p78xxKi5Ipz5Fbx9H
"""

from google.colab import drive
drive.mount('/content/gdrive')

import os
import numpy as np
import pandas as pd
import keras

os.chdir("/content/gdrive/My Drive/Colab Notebooks/cataract")
os.getcwd()

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.optimizers import Adam

classifier = Sequential()
classifier.add(Convolution2D(32,3,3, input_shape=(64,64,3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Convolution2D(32,3,3,activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Flatten())

classifier.add(Dense(output_dim=128,activation='relu'))
classifier.add(Dense(output_dim=1 ,activation='sigmoid'))

classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics = ['accuracy'])

from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)


training_set = train_datagen.flow_from_directory('/content/gdrive/My Drive/Colab Notebooks/cataract/Train-new',
                                                   target_size=(64, 64),
                                                    batch_size=20,
                                                    class_mode='binary')

test_set = test_datagen.flow_from_directory('/content/gdrive/My Drive/Colab Notebooks/cataract/Test-new',
                                                target_size=(64, 64),
                                                 batch_size=20,
                                                 class_mode='binary')

history =classifier.fit_generator(training_set,steps_per_epoch=8068,epochs=2,validation_data=test_set,nb_val_samples=1600)

vgg16_classifier= keras.applications.vgg16.VGG16()
vgg16_classifier.summary()
type(vgg16_classifier)
classifier=Sequential()
for layer in vgg16_classifier.layers:
    classifier.add(layer)
    
classifier.summary()
classifier.layers.pop()
classifier.summary()
for layer in classifier.layers:
    layer.trainable=False

classifier.summary()

classifier.compile(Adam(lr=.0001),loss='binary_crossentropy',metrics=['accuracy'])

from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)


training_set = train_datagen.flow_from_directory('/home/shubhangi/Documents/CataractDetectionApp-UsingCNN-NeuralNetwork-master/Train',
                                                   target_size=(64, 64),
                                                    #batch_size=9,
                                                    batch_size=855,
                                                    class_mode='binary')

test_set = test_datagen.flow_from_directory('/home/shubhangi/Documents/CataractDetectionApp-UsingCNN-NeuralNetwork-master/Test',
                                                target_size=(64, 64),
                                                 #batch_size=9,
                                                 batch_size=20,
                                                 class_mode='binary')

history =classifier.fit_generator(training_set,
                            steps_per_epoch=4,epochs=5
                            validation_data=test_set,
                            nb_val_samples=80
                            )

classifier.summary()