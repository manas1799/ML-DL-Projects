import cv2
import numpy as np 
import os 

def distance(v1, v2):
	# Eucledian 
	return np.sqrt(((v1-v2)**2).sum())

def knn(train, test, k=5):
	dist = []
	
	for i in range(train.shape[0]):
		# Get the vector and label
		ix = train[i, :-1]
		iy = train[i, -1]
		# Compute the distance from test point
		d = distance(test, ix)
		dist.append([d, iy])
	# Sort based on distance and get top k
	dk = sorted(dist, key=lambda x: x[0])[:k]
	# Retrieve only the labels
	labels = np.array(dk)[:, -1]
	
	# Get frequencies of each label
	output = np.unique(labels, return_counts=True)
	# Find max frequency and corresponding label
	index = np.argmax(output[1])
	return output[0][index]
################################


#Init Camera

# Face Detection

def predict(face):
	face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_alt.xml')

	#skip = 0
	dataset_path = r'--path to your faces dataset'

	face_data = [] 
	labels = []

	class_id = 0 # Labels for the given file
	names = {} #Mapping btw id - name


# Data Preparation
	for fx in os.listdir(dataset_path):
		if fx.endswith('.npy'):
		#Create a mapping btw class_id and name
			names[class_id] = fx[:-4]
			print("Loaded "+fx)
			data_item = np.load(dataset_path+fx)
			face_data.append(data_item)

		#Create Labels for the class
			target = class_id*np.ones((data_item.shape[0],))
			class_id += 1
			labels.append(target)

	face_dataset = np.concatenate(face_data,axis=0)
	face_labels = np.concatenate(labels,axis=0).reshape((-1,1))

	#print(face_dataset.shape)
	#print(face_labels.shape)

	trainset = np.concatenate((face_dataset,face_labels),axis=1)
	print(trainset.shape)

# Testing 


	#Predicted Label (out)
	out = knn(trainset,face.flatten())

	#Display on the screen the name and rectangle around it
	pred_name = names[int(out)]
	
	#print(str(pred_name))
	return str(pred_name)



