from flask import Flask, render_template as template
from flask_assets import Bundle, Environment

app = Flask(__name__)

assets = Environment(app)
css = Bundle('src/main.css', output='dist/main.css')
js = Bundle("src/*.js", output="dist/main.js")

assets.register('css', css)
assets.register("js", js)
css.build()
js.build()

@app.route('/')
def index():
    return template('index.html')

@app.route('/users')
def users():
    return '<p>Users</p>'

