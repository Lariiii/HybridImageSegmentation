import os

from flask import *
import approach_shapeMatching

from werkzeug.utils import secure_filename

from read_files import read_generic
from dataframeToImage import dataframeToImage
from dataPreprocessing import pruning

# temp directory needs to be created in the webserver root (because of the file location, this is the 'web' directory)
UPLOAD_FOLDER = 'temp'
ALLOWED_EXTENSIONS = {'txt'}


def createApp(debug=True):
    """
    :param debug: whether the Flask app should be in debug mode (disable for deployment!!!)
    :return: a configured, not yet started Flask app
    """
    app = Flask(__name__, static_url_path='')
    app.debug = debug
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    return app


app = createApp()


@app.route('/')
def root():
    # For any direct call, return the main page 'bootstrap.html'
    defaultFile = 'bootstrap.html'

    return app.send_static_file(defaultFile)


@app.route('/temp/<path:path>')
def serveTemp(path):
    # For any request to the temp directory, return the found file
    return send_from_directory('temp', path)


def allowed_file(filename):
    # Do some basic extension filtering
    # Return Boolean
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploaddata', methods=['GET', 'POST'])
def upload():
    # Serve the uploading interface
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
        # respond with a basic upload page
        return get_response

    data = request.get_data()
    # print(data)

    # make it compatible to both curl- and browser-uploaded POST-requests
    fileAttribute = 'file'
    dataAttribute = 'data'
    if fileAttribute in request.files:
        file = request.files[fileAttribute]
    elif dataAttribute in request.files:
        file = request.files[dataAttribute]
    else:
        # redirect to root
        return redirect(url_for('root'))

    # if user does not select file, browser also
    # submits an empty part without filename
    if file.filename == '':
        # redirect to root
        return redirect(url_for('root'))

    if file and allowed_file(file.filename):
        # save uploaded file to temp directory
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        print('File saved to ', filepath)

        targetFilename = ''.join(filename + '.png')
        targetFilepath = os.path.join(app.config['UPLOAD_FOLDER'], targetFilename)

        targetUrl = '/'.join(['', app.config['UPLOAD_FOLDER'], targetFilename])

        # if the target image has not already been computed, create it (convert the uploaded data to an image file)
        if not os.path.isfile(targetFilepath):
            print('Store image to ', targetFilename)
            df = read_generic(filepath)
            df_pruned = pruning(df)
            dataframeToImage(df_pruned, targetFilepath)

        # return the download URL for the image matching the uploaded data
        response = targetUrl

        return response
    return get_response


@app.route('/mergefiles')
def mergeFiles():
    """
    Transform an uploaded file with shapeMatching approach.
    Until now, it was not possible to make it run (only within the main.py-main method), so the resulting image was
    pasted into the temp directory and a static download URL was returned.
    :return:
    """
    filename = request.args.get('f1')
    basePath = os.path.dirname(os.path.realpath(__file__))
    print(os.path.dirname(os.path.realpath(__file__)))
    print(filename)

    return 'temp/Corine.txt.png_merged.png'
    targetFilename = ''.join([filename, '_', 'merged.png'])
    # targetFilepath = os.path.join(app.config['UPLOAD_FOLDER'], targetFilename)

    filename = os.path.join(basePath, filename)
    targetFilepath = os.path.join(basePath, targetFilename)
    print(filename)
    print(targetFilepath)

    # crashes...
    approach_shapeMatching.run(filename, subjectiveIntegration=True, show=False, outputPath=targetFilepath)

    print('Transformed image to ', targetFilename)
    response = '/'.join(['', app.config['UPLOAD_FOLDER'], targetFilename])
    return response


if __name__ == "__main__":
    """
    This call has to be the last, otherwise not all routes will be known
    """
    app.run()
