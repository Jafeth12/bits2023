from flask import render_template, request, jsonify, url_for
from dracula import app, db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    return '<p>Users</p>'

