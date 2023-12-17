from sqlalchemy.orm import Mapped, mapped_column
from dracula import app
from dracula.db import db

class Sample(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    # filename: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)
    filename: Mapped[str] = mapped_column(db.String(80), nullable=False) # deberia ser unique pero sudaa
    score: Mapped[int] = mapped_column(db.Integer, nullable=False)
    percentage: Mapped[int] = mapped_column(db.Integer, nullable=False)
    day_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('day.id'), nullable=False)

    def __init__(self, filename, score, percentage, day_id):
        self.filename = filename
        self.score = score
        self.day_id = day_id
        self.percentage = percentage

class Day(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    date: Mapped[str] = mapped_column(db.String(80), unique=True, nullable=False)
    cicle_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('cicle.id'), nullable=False)

    def __init__(self, date, cicle_id):
        self.date = date
        self.cicle_id = cicle_id

class Cicle(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    is_active: Mapped[bool] = mapped_column(db.Boolean, default=True)

with app.app_context():
    db.create_all()
# Add Cicles
#     for i in range(1, 3):
#         db.session.add(Cicle())
#
# # Add Days
#     day = 16
#     for i in range(0, 6):
#         for j in range(1, 3):
#             day += 1
#             print(str(day) + "/12/2023" + " " + str(j))
#             db.session.add(Day(str(day) + "/12/2023", j))

# Add Samples
    # for i in range(1, 3):
    #     db.session.add(Sample("example/path", 20, i))

    # db.session.commit()


