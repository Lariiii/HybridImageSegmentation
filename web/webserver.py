from flask import Flask

def createApp(debug=True):
    app = Flask(__name__)
    app.debug=debug
    return app

app = createApp()

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()