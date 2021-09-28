import os
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
from pythonwork import *

UPLOAD_FOLDER = 'C:/Users/pharsh/Desktop/MyFiles/pythoncode/transferworkproject2/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt', 'xlsx'}
app.secret_key = "dont tell anyone"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('no file uploaded', "error")
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash("Invalid File")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filepath = request.form['text']
            if filepath == '':
                flash("Not A Valid Filepath")
                return redirect(request.url)
            if filepath != '':
                pythonfunction(fr'C:\Users\pharsh\Desktop\MyFiles\pythoncode\transferworkproject2\uploads\{filename}', filepath)
                ##flash('your file is now available for use at the path specified', "info")
                redirect(url_for('download_file', name=filename))
                return redirect(request.url)
    return render_template('index.html')

from flask import send_from_directory

@app.route('/uploads/<name>')
def download_file(name):
    send_from_directory(app.config["UPLOAD_FOLDER"], name)
    deleteupload(fr'C:\Users\pharsh\Desktop\MyFiles\pythoncode\transferworkproject2\uploads\{name}')
    return render_template('index.html')

@app.route('/instructions.html')
def show_instructions():
    return render_template('instructions.html')
if __name__ == '__main__':
    app.run(debug=True)