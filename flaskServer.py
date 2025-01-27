from flask import Flask
import startScript
import stopScript

app = Flask(__name__)

@app.route('/')
def index():
    return '''<p>Index Page
    <a href="/start"><button>Start</button></a>
    <a href="/stop"><button>Stop</button></a>
        </p>'''

@app.route('/start')
def start():
    startScript.start()
    return '''<p>Start Page</p>
        <a href="/"><button>Index</button></a>
        '''

@app.route("/stop")
def stop():
    stopScript.stop()
    return '''<p>Stop page<p>
        <a href="/"><button>Index</button></a>
        '''