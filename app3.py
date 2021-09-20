import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from pythonwork import *

UPLOAD_FOLDER = 'C:/Users/pharsh/Desktop/MyFiles/python/transferworkproject/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt', 'xlsx'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filepath = request.form['text']
            pythonfunction(fr'C:\Users\pharsh\Desktop\MyFiles\python\transferworkproject\uploads\{filename}', filepath)
            return redirect(url_for('download_file', name=filename))
    return render_template('index.html')

from flask import send_from_directory

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

if __name__ == '__main__':
    app.run(debug=True)