from flask import Flask
from flask_assets import Bundle, Environment
from dracula.db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dracukeo.db'

db.init_app(app)

assets = Environment(app)
css = Bundle('src/main.css', output='dist/main.css')
js = Bundle("src/*.js", output="dist/main.js")

assets.register('css', css)
assets.register("js", js)
css.build()
js.build()

from dracula import routes, models
