from keras.layers import *
from keras.layers.advanced_activations import LeakyReLU
from keras.models import Sequential,Model
from keras.optimizers import Adam
from keras.preprocessing import image
from keras import models
import matplotlib.pyplot as plt
import math
import numpy as np
import cv2

def fun(img):
	img = image.load_img(img, target_size=(224,224))
	img = image.img_to_array(img)
	img = np.asarray(img)
	img = img.astype(np.float32)/255.0
	model = models.load_model('Weights/autoencoder2_800.h5')
	pred_img = model.predict(img.reshape((1,224,224,3)))
	pred_img = pred_img.reshape((224,224,3))
	while True:
		cv2.imshow("Frame",pred_img)
		key_pressed = cv2.waitKey(1) & 0xFF
		if key_pressed == ord('q'):
			break

	print(pred_img.shape)




#fun('img_test.jpg')