from flask import render_template
from ugnius import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projects')
def projects():
    return render_template('projects.html', heading='Projects')


@app.route('/library')
def library():
    return render_template('index.html')


@app.route('/coursework')
def coursework():
    return render_template('coursework.html', heading='Coursework')


@app.route('/experience')
def experience():
    return render_template('experience.html', heading='Experience')
