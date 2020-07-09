import cv2
import numpy as np 
import os 
from keras.models import load_model
cap = cv2.VideoCapture(0)

# Face Detection
face_cascade = cv2.CascadeClassifier(r"haarcascade_frontalface_alt.xml")


while True:
	ret,frame = cap.read()
	if ret == False:
		continue

	faces = face_cascade.detectMultiScale(frame,1.3,5)
	if(len(faces)==0):
		continue
	model = load_model(r'mask_model.h5')
	val = 0
	for face in faces:
		x,y,w,h = face

		#Get the face ROI
		offset = 20
		face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset]
		face_section = cv2.resize(face_section,(90,90))
		face_section = face_section/255.0
		#np.save('My_face',face_section)
		face_section = face_section.reshape((1,90,90,3))
		val = model.predict(face_section)
		print(val)
		if val<0.5:
			pred_name = 'mask'
		else:
			pred_name = 'no mask'

		cv2.putText(frame,pred_name,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)


	cv2.imshow("Faces",frame)

	key = cv2.waitKey(1) & 0xFF
	if key==ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
