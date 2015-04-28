# -*- coding: utf-8 -*-
__author__ = 'kiwi'

from flask import Flask
from flask import make_response

app = Flask(__name__)


@app.route('/')
def index():  # view function
    return '<h1>Hello World!</h1>', 400
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


@app.route('/user/<name>')  # display the name on it
def user(name):
    return '<h1>Hello, %s!</h1>' % name

from flask import redirect
@app.route('/')
def index():
    return redirect('http://www.example.com')

from flask import abort
@app.route('/user/<id>')    # log in function
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello,%s</h1>' % name

# for extension
from flask.ext.script import Manager
manager = Manager(app)


from flask import Flask, render_template
    #...

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

if __name__ == '__main__':  # Running on http://127.0.0.1:5000/ restarting with reloader
    app.run(debug=True)