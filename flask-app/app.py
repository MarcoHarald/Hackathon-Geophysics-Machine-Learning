from flask import Flask
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

def mlquery(query):
    return [
        (0.9, 'foo.pdf'),
        (0.8, 'bar.tif'),
        (0.7, 'baz.tif'),
        (0.6, 'bar.tif'),
        (0.5, 'something.pdf'),
        (0.4, 'somethngelse.tif'),
        (0.3, 'help,pdf'),
        (0.2, 'eek.pdf'),
        (0.1, 'crikey.tif'),
        (0.05, 'last_one.pdf')]

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q')
    results = mlquery(query)
    return render_template('results.html', query=query, results=results)