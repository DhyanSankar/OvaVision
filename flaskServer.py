from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print('on the hompage')
    return '''<p>Index Page
    <a href="/start"><button>Start</button></a>
    <a href="/stop"><button>Stop</button></a>
        </p>'''

@app.route('/start')
def start():
    print('on the start page')
    return '''<p>Start Page</p>
        <a href="/"><button>Index</button></a>
        '''

@app.route("/stop")
def stop():
    print("on the stop page")
    return '''<p>Stop page<p>
        <a href="/"><button>Index</button></a>
        '''