import keras.backend.tensorflow_backend as tb
tb._SYMBOLIC_SCOPE.value = True
from tensorflow.keras.models import load_model
import internal
import face_recognition
from flask import Flask, render_template, request, redirect
import time
import cv2
import numpy as np
import edit_dictionary
import send_OTP
import alphabet
import face_data_collection
import caption_it

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("file1.html")



@app.route('/enter_OTP')
def fun():
	
	otp_received = otp_list[-1]
	string = alphabet.main()
	if otp_received == string :
		return "<h1>Login Successful!</h1>"
	return "Error!"




@app.route('/register')

def new_user():
	name = input("Enter your name : ")
	
	email = input("Enter you email : ")
	face_data_collection.utility(file_name=name)
	edit_dictionary.edit_in_dictionary(name,email)
	face_data_collection.utility(name)
	return render_template("file3.html")


otp_list = []


@app.route('/identification')
def testfun():

	#cap = cv2.VideoCapture(0)
	data = internal.capture()
	#cap.release()
	cv2.destroyAllWindows()
	data = np.asarray(data)
	name ="Default"
	if not data.size==0 :
		
		#while True:
		#	cv2.imshow("Frame",data)

		#	key_pressed = cv2.waitKey(1) & 0xFF

		#	if key_pressed == ord('q'):
		#		break

		name = face_recognition.predict(face=data)

		name_low = name.lower()

		email = edit_dictionary.get_email(name=name_low)

		otp = send_OTP.workfun(email)

		otp_list.append(otp)		

		if name is not "Default":

			return render_template("identify.html", name = name,email=email )
		


	return "Error!! Try again!"

@app.route('/caption_img')
def cap1():
	return render_template("caption.html")



@app.route('/caption_img', methods = ['POST'])
def cap():
	if request.method == 'POST':

		f= request.files['userfile']
		path = './static/{}'.format(f.filename)
		f.save(path)

		caption = caption_it.caption_this_image(path)

		result_dic = {
		'image' : path,
		'caption' : caption
		}

	return render_template("caption.html")


if __name__ == '__main__':
	# app.debug = True
	app.run(threaded=False)









