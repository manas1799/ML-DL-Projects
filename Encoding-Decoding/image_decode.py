import keras.backend.tensorflow_backend as tb
tb._SYMBOLIC_SCOPE.value = True
import tensorflow as tf
from tensorflow.keras.layers import *
from keras.layers.advanced_activations import LeakyReLU
from tensorflow.keras.models import Sequential,Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import math
import numpy as np
import cv2

def decode(path):

	#img_name = img_name+'.npy'
	pred = np.load(path)
	pred = np.asarray(pred)
	#print(pred.shape())
	idx = -11  # index of desired layer
	autoencoder2 = load_model('autoencoder2_1100.h5')
	input_shape = autoencoder2.layers[idx].get_input_shape_at(0)
	layer_input = Input(shape=input_shape) 
	
	x = layer_input
	
	for layer in autoencoder2.layers[idx:]:
		x = layer(x)

# create the model
	new_model = Model(layer_input, x)
	pred= pred.reshape((1,1,2048))
	img = new_model.predict(pred)
	img = img.reshape((224,224,3))
	while True:
		cv2.imshow("Video Frame",img)

	#Wait for user input - q, then you will stop the loop
		key_pressed = cv2.waitKey(1) & 0xFF
		if key_pressed == ord('q'):
			break



