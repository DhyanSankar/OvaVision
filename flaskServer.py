# flask --app flaskServer run
# cd ovavision-frontend + npm start
from flask import Flask, jsonify
from flask_cors import CORS
import startScript
import stopScript
import visualization.EggBinCollection as EggBinCollection

app = Flask(__name__)
CORS(app)

status = {"state": "Stopped"}  # Default state
bin = EggBinCollection.EggBinCollection(3, 4, 1, None)

@app.route('/status')
def get_status():
    bin_status = bin.print_status()
    return jsonify({"status": status["state"], "bin_status": bin_status})

@app.route('/start')
def start():
    global status
    startScript.start()
    status["state"] = "Running"
    return jsonify({"message": "Start script executed", "status": status["state"]})

@app.route('/stop')
def stop():
    global status
    stopScript.stop()
    status["state"] = "Stopped"
    return jsonify({"message": "Stop script executed", "status": status["state"]})

if __name__ == '__main__':
    app.run(debug=True)
