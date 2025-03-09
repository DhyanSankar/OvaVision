# flask --app backend/flaskServer run
# cd ovavision-frontend + npm start
from flask import Flask, jsonify, request
from flask_cors import CORS
import startScript
import stopScript
import sys
import os

# Add the root directory to sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)



import backend.visualization.EggBinCollection as EggBinCollection

app = Flask(__name__)
CORS(app)

status = {"state": "Stopped"}  # Default state
machine = EggBinCollection.EntireMachinery(3, 4)

@app.route('/status')
def get_status():
    machine_status = machine.print_status()
    return jsonify({"status": status["state"], "bin_status": machine_status})

@app.route('/start')
def start():
    global status
    status["state"] = "Running"
    startScript.start()
    return jsonify({"message": "Start script executed", "status": status["state"]})

@app.route('/stop')
def stop():
    global status
    status["state"] = "Stopped"
    stopScript.stop()
    return jsonify({"message": "Stop script executed", "status": status["state"]})

@app.route('/moveArm', methods=['POST'])
def move_arm():
    global status
    status["state"] = "Running"
    data = request.json
    x = data.get('x')
    r = data.get('r')
    z = data.get('z')
    bin.setxrz(x, r, z)
    return jsonify({"message": "Set position executed", "status": status["state"]})


if __name__ == '__main__':
    app.run(debug=True)
