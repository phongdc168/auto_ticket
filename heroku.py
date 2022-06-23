from xxlimited import Null
from flask import Flask, jsonify, render_template, request, redirect, flash
from sklearn.utils import resample
from werkzeug.utils import secure_filename
import main,json
import os 
app = Flask(__name__)
UPLOAD_FOLDER = 'static/images/'
app.secret_key = "secret key"

#Define the upload folder to save images uploaded by the user. 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#Add Post method to the decorator to allow for form submission. 
@app.route('/', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)  #Use this werkzeug method to secure filename. 
            label = main.predict(filename)
            return label
          
if __name__ == "__main__":
    app.run(debug=True)
