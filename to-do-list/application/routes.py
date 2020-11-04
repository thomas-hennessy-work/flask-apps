from flask import render_template, redirect, url_for

from application import db, app
from application.models import Todos
from application.forms import ToDoForm

@app.route('/')
def index():
    all_todos = Todos.query.all()
    return render_template('index.html', all_todos=all_todos)

@app.route('/add', methods=['GET','POST'])
def add():
    form = ToDoForm()
    if form.validate_on_submit():
        new_todo = Todos(task=form.task.data)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/complete/<int:todo_id>')
def complete(todo_id):
    todo_to_update = Todos.query.get(todo_id)
    todo_to_update.complete = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/incomplete/<int:todo_id>')
def incomplete(todo_id):
    todo_to_update = Todos.query.get(todo_id)
    todo_to_update.complete = False
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<task>')
def update(task):
    todo_to_update = Todos.query.first()
    todo_to_update.task = task
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo_to_delete = Todos.query.get(todo_id)
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect(url_for('index'))
