import os
from werkzeug.utils import secure_filename
from urllib.request import Request
from flask import Flask, render_template, Response, request, redirect, flash
#from Myfunctions import *
import urllib
import secrets
import cv2

secret = secrets.token_urlsafe(32)
UPLOAD_FOLDER = 'static/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app = Flask(__name__)
app.secret_key = secret
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    """my main page"""
    return render_template('index.html')


@app.route('/UploadImage', methods=['POST'])
def UploadImage():
    """the upload image page"""
    return render_template('imageupload.html')


@app.route('/UploadImageFunction', methods=['POST'])
def UploadImageFunction():
    if request.method == 'POST':

        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # If user uploads the correct Image File
        if file and allowed_file(file.filename):

            # Pass it a filename and it will return a secure version of it.
            # The filename returned is an ASCII only string for maximum portability.
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            results = image_preprocessing(filename)
            if results is None:
                return render_template('Error.html')
            else:

                img_preds = results[0]
                frame = results[1]
                faces_detected = results[2]

                results2 = predictions_results(img_preds, frame, faces_detected, filename)
                full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)

                return render_template('imageupload.html', user_image=full_filename,
                                       number_of_face="Total Number of faces detected : {}".format(results2[0]),
                                       no_mask_face="Total Number of faces without nose mask : {}".format(results2[1]),
                                       correct_mask_face="Total Number faces with mask : {}".format(results2[2]),
                                       incorrect_mask_face="Total Number of faces inappropraitely wearing face  mask : {}".format(results2[3]))



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=88)
