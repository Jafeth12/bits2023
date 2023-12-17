from sqlalchemy.orm import Mapped, mapped_column
from dracula import app
from dracula.db import db

class Sample(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    filename: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)
    score: Mapped[int] = mapped_column(db.Integer, nullable=False)
    day_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('day.id'), nullable=False)

class Day(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    date: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)
    cicle_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('cicle.id'), nullable=False)

class Cicle(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)

    def __init__(self, id):
        self.id = id

with app.app_context():
    db.create_all()

