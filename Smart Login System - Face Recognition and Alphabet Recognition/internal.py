import cv2
import numpy as np
import time 
#Init Camera

def capture():
	

# Face Detection
	cap = cv2.VideoCapture(0)
	face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_alt.xml')

	skip = 0
	face_data = []
	dataset_path = r'--path to pictures folder'
	#file_name = input("Enter the name of the person : ")

	while True:
		ret,frame = cap.read()

		if ret==False:
			print("camera error!!")
			return

		time.sleep(5)

		faces = face_cascade.detectMultiScale(frame,1.3,5)
		if len(faces)==0:
			cap.release()
			cv2.destroyAllWindows()
		
		faces = sorted(faces,key=lambda f:f[2]*f[3])

	# Pick the last face (because it is the largest face acc to area(f[2]*f[3]))
		for face in faces[-1:]:
			x,y,w,h = face
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
			#Extract (Crop out the required face) : Region of Interest
			offset = 10
			face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset]
			face_section = cv2.resize(face_section,(100,100))

			face_data.append(face_section)

			break
		break

	if len(face_data) > 0:
		face = face_data[0]
		face_data = np.asarray(face_data)
		face_data = face_data.reshape((100,100,3))

		#print(face_data.shape)


# Save this data into file system
	np.save(dataset_path+file_name+'.npy',face_data)
	print("Data Successfully save at "+dataset_path+file_name+'.npy')

	while True:
		cv2.imshow("Frame",face_data)
		key_pressed = cv2.waitKey(1) & 0xFF
		if key_pressed == ord('q'):
			cap.release()
			cv2.destroyAllWindows
			break
				

	cap.release()
	cv2.destroyAllWindows()																					
	return face_data

