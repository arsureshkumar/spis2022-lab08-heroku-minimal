# This repl.it is intended for publishing to Heroku
from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloRoot():
    return f'''
    <h1>Congratulations!</h1>
    <p>You are up and running.</p>
    '''

if __name__=="__main__":
    app.run(host='0.0.0.0')