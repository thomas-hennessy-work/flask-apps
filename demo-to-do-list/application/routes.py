from flask import render_template, redirect, url_for

from application import db, app
from application.models import Todos

@app.route('/')
def index():
    all_todos = Todos.query.all()
    return render_template('index.html', all_todos=all_todos)

@app.route('/add')
def add():
    new_todo = Todos(task='New Todo')
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))
