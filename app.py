from ast import Return
from crypt import methods
from django.shortcuts import render
from flask import Flask,flash,request,redirect,url_for,render_template
from urllib3 import Retry
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "cairocoders-ednalan"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOW_EXTENSIONS = set(['png','jpg','gif'])
    
def allowed_file(filename):
    return '.' in filename and filename.risplit('.',1)[1].lower()

@app.route('/')
def home():
    return render_template('index.html')
      
@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.flame == '':
        flash('No image selected for upload')
        return redirect(request.url)
     
    if __name__ == "_main_":
         app.run()