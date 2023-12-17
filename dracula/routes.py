import os
from flask import render_template, request, jsonify, url_for
from dracula import app, db
from dracula.quiz import questions, determine_alert 

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/uploads')
def uploads():
    return render_template('uploads.html')

@app.route('/quiz/<int:cicle_id>')
def quiz(cicle_id):
    cicle_score = get_cicle_score(cicle_id)
    return render_template('samanta_quiz.html', quest=questions, score=cicle_score)

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

@app.route('/quiz_submit', methods=['POST'])
def quiz_submit():
    return determine_alert(request.form)

 







