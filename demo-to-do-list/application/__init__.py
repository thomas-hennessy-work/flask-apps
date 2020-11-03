from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = flask(__name__)

db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
