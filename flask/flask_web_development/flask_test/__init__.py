# -*- coding: utf-8 -*-
__author__ = 'kiwi'

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index(): # view function
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':   # Running on http://127.0.0.1:5000/ restarting with reloader
    app.run(debug=True)

