from application import db
from datetime import datetime

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(127), nullable=False)
    complete = db.Column(db.Boolean, default=False)
    dateAdded = db.Column(db.Date, nullable=False)
