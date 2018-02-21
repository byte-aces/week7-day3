#!/usr/bin/env python3

from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def show_homepage():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def show_loginpage():
    if request.method == 'GET':
        return render_template('sample.html')
    else:
        # This is control flow to handle a POST request
        username = request.form['username']
        password = request.form['password']
        # print(username)
        # print(password)
        if username == 'guido@python.org' and password == 'hobgoblin':
            return render_template('dashboard.html')
        else:
            return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
