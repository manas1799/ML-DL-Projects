from flask import Flask, render_template, request, redirect
import image_encode
from werkzeug import secure_filename
import os
import image_decode

UPLOAD_FOLDER = 'Uploads/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ENCODING_FOLDER = 'Encodings/'
app.config['ENCODING_FOLDER'] = ENCODING_FOLDER



@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/',methods = ['POST'])
def hello1():
	f = request.files['userfile']
	path = "./static/{}".format(f.filename)# ./static/images.jpg
	f.save(path)
	print("Path : "+path)
	#filename = secure_filename(f.filename)
	name = image_encode.fun(path)
	print("Name is : " + str(name))
	full_name = os.path.join(app.config['ENCODING_FOLDER'], name)
	print(full_name)


	return render_template("encoded-download.html",name=full_name)


@app.route('/decode')
def upload_file():
   return render_template('decode_idx.html')
	
@app.route('/decoder', methods = ['POST'])
def upload_file_():
   if request.method == 'POST':
      f = request.files['file']
      filename = secure_filename(f.filename)
      path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
      f.save(path)
      print(path)
      image_decode.decode(path)
      return 'file uploaded successfully'



if __name__ == '__main__':
	# app.debug = True
	app.run(debug = True, threaded = False)
