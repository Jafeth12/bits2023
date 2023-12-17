import os
from flask import render_template, request, jsonify, url_for
from dracula import app, db
from dracula.models import Cicle, Day, Sample
from dracula.quiz import questions
from dracula.image_detection import get_score

@app.route('/')
def index():
    return home()

@app.route('/home')
def home():
    cicles = Cicle.query.all()
    punts = []
    for cicle in cicles:
        punts.append(get_cicle_score(cicle))
    cicles_with_scores = zip(cicles, punts)
    return render_template('home.html', cicles_with_scores=cicles_with_scores)

@app.route('/cicle/<int:id>')
def cicle(id):
    cicle = Cicle.query.filter_by(id=id)

    if cicle.count() == 0:
        return 'Cicle not found'

    days = Day.query.filter_by(cicle_id=id)
    samples = Sample.query.all()

    return render_template('cicle.html', cicle=id, days=days, samples=samples)

@app.route('/quiz')
def quiz():
    return render_template('samanta_quiz.html', quest=questions)

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

@app.route('/newcicle', methods=['PUT'])
def new_cicle():
    cicle = Cicle()
    db.session.add(cicle)
    db.session.commit()
    return 'Afegir cicle';

@app.route('/new_day/<int:cicle_id>')
def new_day(cicle_id):
    return render_template('new_day.html', cicle_id=cicle_id)

@app.route('/create_day/', methods=['POST'])
def create_day():
    cicle_id = request.form['cicle_id']
    day = request.form['day']
    day = Day(day, cicle_id)

    print(request)

    if 'file' not in request.files:
        # ERR: No file in request
        return '<p>No file recieved</p>'
    else:
        file = request.files['file']
        filename = file.filename or ''
        path = os.path.join('dracula/static/upload', filename)
        file.save(path)

    score, percentage = get_score(path)

    sample = Sample(filename, score, percentage, day.id)

    db.session.add(day)
    db.session.add(sample)

    db.session.commit()

    return 'Dia creat'

# @app.route('/dbg', methods=['GET'])
# def dbg():
#     sample = Sample('sample_xd', 88, 1)
#     db.session.add(sample)
#     db.session.commit()
#     return 'a'

# Hacer el sumatorio de los scores de los samples de un ciclo
def get_cicle_score(cicle):
    days = Day.query.filter_by(cicle_id=cicle.id)
    total = 0
    for day in days:
        samples = Sample.query.filter_by(day_id=day.id)
        for sample in samples:
            total += sample.score
    return total


