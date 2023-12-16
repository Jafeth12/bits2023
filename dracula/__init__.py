import os
from flask import Flask, render_template as template, request
from flask_assets import Bundle, Environment

app = Flask(__name__)

assets = Environment(app)
css = Bundle('src/main.css', output='dist/main.css')
js = Bundle("src/*.js", output="dist/main.js")

assets.register('css', css)
assets.register("js", js)
css.build()
js.build()

# === Routes ===

@app.route('/')
def index():
    return template('index.html')


# === Endpoints ===

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
