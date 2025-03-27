# flask --app flaskServer run
# OR
# python -m flask --app flaskServer run
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
import backend.visualization.EggSorter as EggSorter


app = Flask(__name__)
CORS(app)

status = {"state": "Stopped"}  # Default state

initial_arr = [
            [["m", "m", "m", "m"], ["f", "f", "f", "f"]],
            [["m", "m", "m", "m"], ["f", "f", "f", "f"]],
            [["0", "0", "0", "0"], ["0", "0", "0", "0"]],
        ]

sorter = EggSorter.EggSorter()
sorter.initialize(initial_arr)
machine = EggBinCollection.EntireMachinery(initial_arr, sorter=sorter)

@app.route('/status')
def get_status():
    machine_status = machine.print_status()
    sorter_status = sorter.run_alg(initial_arr)
    print("sorter status", sorter_status)
    return jsonify({"status": status["state"], "bin_status": machine_status + '\n' + "Sort operations: \n" + sorter_status})

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

@app.route('/moveEgg', methods=['POST'])
def move_egg():
    global status
    status["state"] = "Running"
    data = request.json
    incubator = int(data.get('incubator'))
    layer = int(data.get('layer'))
    location = int(data.get('location'))
    target_incubator = int(data.get('target_incubator'))
    target_layer = int(data.get('target_layer'))
    target_location = int(data.get('target_location'))
    
    # Create the command in the required format
    command = [[layer, incubator, location], [target_layer, target_incubator, target_location]]
    
    # Execute the egg movement using EggSorter
    sorter.execute_egg_movement(command)
    return jsonify({"message": "Egg moved successfully", "status": status["state"]})


if __name__ == '__main__':
    app.run(debug=True)
