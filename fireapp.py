import yolo
from flask import Flask, render_template, request, send_from_directory, send_file, Response, jsonify
import os
from flask_cors import CORS, cross_origin
from flask import request

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

app = Flask(__name__)

RENDER_FACTOR = 35

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

@app.route("/")
def home():
    # return "home Page"
    return render_template("index.html")

@app.route("/predict")
@cross_origin()
def predict():
    # return detection window
    detection=os.system("python3 yolo.py --webcam False")
    return detection


@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == "__main__":
    app.run(debug=True,port=8000)

