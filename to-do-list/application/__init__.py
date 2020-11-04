from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SOME_KEY'

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = ''

from application import routes
