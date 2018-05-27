import os

from flask import *
import approach_shapeMatching

from werkzeug.utils import secure_filename

from read_files import read_generic
from dataframeToImage import dataframeToImage
from dataPreprocessing import pruning

UPLOAD_FOLDER = 'temp'
ALLOWED_EXTENSIONS = {'txt'}


def createApp(debug=True):
    app = Flask(__name__, static_url_path='')
    app.debug = debug
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    return app


app = createApp()


@app.route('/')
def root():
    defaultFile = 'bootstrap.html'

    return app.send_static_file(defaultFile)

@app.route('/temp/<path:path>')
def serveTemp(path):
    return send_from_directory('temp', path)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploaddata', methods=['GET','POST'])
def upload():
    get_response = '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <p><input type=file name=file>
             <input type=submit value=Upload>
        </form>
        '''
    if request.method != 'POST':
        return get_response

    data = request.get_data()
    #print(data)

    fileAttribute = 'file'
    dataAttribute = 'data'
    if fileAttribute in request.files:
        file = request.files[fileAttribute]
    elif dataAttribute in request.files:
        file = request.files[dataAttribute]
    else:
        return redirect(url_for('root'))

    # if user does not select file, browser also
    # submit a empty part without filename


    if file.filename == '':
        return redirect(url_for('root'))

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        print('File saved to ', filepath)

        targetFilename = ''.join(filename + '.png')
        targetFilepath = os.path.join(app.config['UPLOAD_FOLDER'], targetFilename)

        targetUrl = '/'.join(['', app.config['UPLOAD_FOLDER'], targetFilename])

        if not os.path.isfile(targetFilepath):
            print('Store image to ', targetFilename)
            df = read_generic(filepath)
            df_pruned = pruning(df)
            dataframeToImage(df_pruned, targetFilepath)
        response = targetUrl

        # call Marvin, get back image path

        return response
    return get_response

@app.route('/mergefiles')
def mergeFiles():
    filename = request.args.get('f1')
    basePath = os.path.dirname(os.path.realpath(__file__))
    print(os.path.dirname(os.path.realpath(__file__)))
    print(filename)

    #return '/temp/Corine.txt.png'
    targetFilename = ''.join([filename, '_', 'merged.png'])
    #targetFilepath = os.path.join(app.config['UPLOAD_FOLDER'], targetFilename)

    filename = os.path.join(basePath, filename)
    targetFilepath = os.path.join(basePath, targetFilename)
    print(filename)
    print(targetFilepath)

    approach_shapeMatching.run(filename, subjectiveIntegration=True, show=False, outputPath=targetFilepath)

    print('Transformed image to ', targetFilename)
    response = '/'.join(['', app.config['UPLOAD_FOLDER'], targetFilename])
    return response


if __name__ == "__main__":
    app.run()
