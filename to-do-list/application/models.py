from application import db

class listItemis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(127) nullable=Flase)
