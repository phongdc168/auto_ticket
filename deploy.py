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

@app.route('/')
def index():
    return render_template('index.html')

#Add Post method to the decorator to allow for form submission. 
@app.route('/', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)  #Use this werkzeug method to secure filename. 
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            # getPrediction(filename)
            label = main.predict(filename)
            flash(label)
            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            flash(full_filename)
            return redirect('/')
if __name__ == "__main__":
    app.run(debug=True)
