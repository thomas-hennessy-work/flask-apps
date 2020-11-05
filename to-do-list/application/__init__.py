from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from os import getenv

app = Flask(__name__)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DB_URI')
from application import routes
