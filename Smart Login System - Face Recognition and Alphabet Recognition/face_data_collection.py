import cv2
import numpy as np
import time

#Init Camera
def utility(file_name):
	cap = cv2.VideoCapture(0)

# Face Detection
	face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_alt.xml')

	skip = 0
	face_data = []
	dataset_path = '--path to your faces dataset'
	

	x = 1
	count = 0
	while True:
		if x==1 :
			x=0
			time.sleep(5)


		ret,frame = cap.read()

		if ret==False:
			continue
	

		faces = face_cascade.detectMultiScale(frame,1.3,5)
		if len(faces)==0:
			continue
		
		faces = sorted(faces,key=lambda f:f[2]*f[3])

	# Pick the last face (because it is the largest face acc to area(f[2]*f[3]))
		for face in faces[-1:]:
			x,y,w,h = face
			offset = 20
			cv2.rectangle(frame,(x-offset,y-offset),(x+offset+w,y+offset+h),(0,255,255),2)

		#Extract (Crop out the required face) : Region of Interest
			
			face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset]
			face_section = cv2.resize(face_section,(100,100))

			skip += 1
			if skip%10==0:
				face_data.append(face_section)
				print(len(face_data))
				count +=1

				


		cv2.imshow("Frame",frame)
		cv2.imshow("Face Section",face_section)

		key_pressed = cv2.waitKey(1) & 0xFF
		if key_pressed == ord('q'):
			break

		if count == 30:
			break

# Convert our face list array into a numpy array
	face_data = np.asarray(face_data)
	face_data = face_data.reshape((face_data.shape[0],-1))
	print(face_data.shape)

# Save this data into file system
	np.save(dataset_path+file_name+'.npy',face_data)
	print("Data Successfully save at "+dataset_path+file_name+'.npy')

	

	cap.release()
	cv2.destroyAllWindows()



