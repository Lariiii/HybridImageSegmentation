import os

from flask import *
import json

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'temp'
ALLOWED_EXTENSIONS = {'txt'}


def createApp(debug=True):
    app = Flask(__name__)
    app.debug = debug
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    return app


app = createApp()


@app.route('/')
def root():
    return 'Hello, World!'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploaddata', methods=['POST'])
def upload():
    #data = request.data
    data = request.get_data()
    #print(data)

    #fileAttribute = 'file'
    fileAttribute = 'data'
    if fileAttribute not in request.files:
        #flash('No file part')
        return redirect(url_for('root'))
    file = request.files[fileAttribute]
    # if user does not select file, browser also
    # submit a empty part without filename


    if file.filename == '':
        #flash('No selected file')
        return redirect(url_for('root'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        targetFilename = ''.join(filename + '.png')
        targetFilepath = os.path.join(app.config['UPLOAD_FOLDER'], targetFilename)

        response = {
            'renderedImage': '/'.join([app.config['UPLOAD_FOLDER'], targetFilename])
        }
        # call Marvin, get back image path

        return json.dumps(response)
    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <p><input type=file name=file>
             <input type=submit value=Upload>
        </form>
        '''

if __name__ == "__main__":
    app.run()
