from flask import Flask, redirect, url_for, render_template, request, jsonify
import json
import sys

# File stuff
localDIR = "./data/"
fileExtension = ".json"

global x
x = 0
vers = str(sys.argv[1]) # gets version from command line when starting

app = Flask(__name__)
# app.config['version'] = vers
# app.run(host='0.0.0.0')

@app.route('/file', methods=['POST'])
def write_file():
    global x
    x += 1
    data = request.json
    firstName = data.get('data').get('firstName')
    lastName = data.get('data').get('lastName')
    with open(localDIR + str(x) + fileExtension, 'wb') as filehandle:
        filehandle.write(request.data)
    return jsonify(
        fileId=str(x)
    )

@app.route('/file/<fileId>', methods=['GET'])
def read_file(fileId):
    contents = open(localDIR+str(fileId)+fileExtension, 'r')
    jsonData = json.load(contents)
    return jsonify(
        jsonData
    )

@app.route('/version', methods=['GET'])
def get_version():
    return jsonify(
        version = app.config["version"]
    )


if __name__ == "__main__":
    # app.run(debug=True)
    app.config['version'] = vers
    app.run(debug=True, host='0.0.0.0')