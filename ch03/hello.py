# -*- coding: utf-8 -*-
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/home')
def home():
    return render_template("index.html")

@app.route('/user/<name>')
def is_user(name):
    return render_template('user.html', user_name=name)

if __name__ == "__main__":
    app.run(debug=True)