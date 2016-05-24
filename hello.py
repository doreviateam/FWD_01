# -*- coding: utf-8 -*-
from flask import Flask, request, redirect
from flask import abort
from flask.ext.script import Manager


app = Flask(__name__)

manager = Manager(app)

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

@app.route("/agent")
def agent():
    user_agent = request.headers.get('User-Agent')
    return "<p>Your brother is {}</p>".format(user_agent)

@app.route("/user/<name>")
def user(name):
    return "<h2>Hello, {}!</h2>".decode("utf-8").format(name)

@app.route('/re')
def google():
    return redirect('http://www.google.fr')

@app.route('/er/<ids>')
def get_user(ids):
    er = "Michel PÖLAC"
    ids = int(ids)
    re = len(er) + ids
    if not id:
        abort(404)
    return '{} + {} = {}'.encode("utf-8").format(er, ids, re)

if __name__ == "__main__":
    manager.run()
    # app.run(debug=True)