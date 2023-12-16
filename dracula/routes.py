import os
from flask import render_template, request, jsonify, url_for
from dracula import app, db
from dracula.models import Cicle, Sample, Day

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/cicle/<int:id>')
def cicle(id):
    return render_template('cicle.html', id=id)

# === Routes ===

@app.route('/users', methods=['GET'])
def users():
    return '<p>Users</p>'

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        # ERR: No file in request
        return '<p>No file recieved</p>'
    else:
        file = request.files['file']
        filename = file.filename or ''
        file.save(os.path.join('dracula/static/upload', filename))
        return '<p>File recieved</p>'
