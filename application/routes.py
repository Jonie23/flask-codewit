from flask import render_template

from application import app

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about/')
def about(): 
    return render_template('about.html')


@app.route('/register/')
def register():
    return render_template('register.html')