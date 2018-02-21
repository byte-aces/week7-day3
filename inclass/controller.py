#!/usr/bin/env python3

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def show_homepage():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def show_loginpage():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
