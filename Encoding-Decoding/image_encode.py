import keras.backend.tensorflow_backend as tb
tb._SYMBOLIC_SCOPE.value = True
from tensorflow.keras.layers import *
from keras.layers.advanced_activations import LeakyReLU
from tensorflow.keras.models import Sequential,Model
from keras.optimizers import Adam
from keras.preprocessing import image
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import math
import numpy as np
import cv2

def fun(img):
	s = img[9:-4]
	print(str(s))
	img = image.load_img(img, target_size=(224,224))
	img = image.img_to_array(img)
	img = np.asarray(img)
	img = img.astype(np.float32)/255.0
	model = load_model('autoencoder2_1100.h5')
	encoder = Model(model.input,model.layers[-12].output)
	pred_img = encoder.predict(img.reshape((1,224,224,3)))
	pred_img = pred_img.reshape((1,2048))
	np.save('Encodings/'+ str(s)+'.npy',pred_img)
	print(pred_img.shape)

	#while True:
	#	cv2.imshow("Frame",pred_img)
	#	key_pressed = cv2.waitKey(1) & 0xFF
	#	if key_pressed == ord('q'):
	#		break

	return (s+'.npy')
