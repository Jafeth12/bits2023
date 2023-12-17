import os
from flask import render_template, request, jsonify, url_for, redirect
from dracula import app, db
from dracula.quiz import questions, determine_alert 
from dracula.models import Cicle, Day, Sample

@app.route('/')
def index():
    return home()

@app.route('/home')
def home():
    cicles = Cicle.query.all()
    punts = []
    for cicle in cicles:
        punts.append(get_cicle_score(cicle.id))
    cicles_with_scores = zip(cicles, punts)
    return render_template('home.html', cicles_with_scores=cicles_with_scores)

@app.route('/cicle/<int:id>')
def cicle(id):
    cicle = Cicle.query.filter_by(id=id)
    days = Day.query.filter_by(cicle_id=id)

    return render_template('cicle.html', cicle=cicle, days=days)

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
    a = determine_alert(request.form)
    return a

@app.route('/newcicle', methods=['PUT'])
def new_cicle():
    cicle = Cicle()
    db.session.add(cicle)
    db.session.commit()
    return 'Afegir cicle'

# @app.route('/dbg', methods=['GET'])
# def dbg():
#     sample = Sample('sample_xd', 88, 1)
#     db.session.add(sample)
#     db.session.commit()
#     return 'a'

# Hacer el sumatorio de los scores de los samples de un ciclo
def get_cicle_score(cicle):
    days = Day.query.filter_by(cicle_id=cicle)
    total = 0
    for day in days:
        samples = Sample.query.filter_by(day_id=day.id)
        for sample in samples:
            total += sample.score
    return total

