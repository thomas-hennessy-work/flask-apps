from flask import render_template, redirect, url_for, request

from datetime import datetime

from application import db, app
from application.models import Todos
from application.forms import ToDoForm, OrderForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = OrderForm()
    totals = {'number_completed':Todos.query.filter_by(complete=True).count(),
            'total':Todos.query.count()
            }
    if form.order.data == "new":
        all_todos = Todos.query.order_by(Todos.id.desc()).all()
    elif form.order.data == "old":
        all_todos = Todos.query.order_by(Todos.id).all()
    elif form.order.data == "completed":
        all_todos = Todos.query.order_by(Todos.complete.desc()).all()
    elif form.order.data == "incompleted":
        all_todos = Todos.query.order_by(Todos.complete).all()
    else:
        all_todos = Todos.query.all()
    return render_template('index.html', all_todos=all_todos, form=form, totals=totals)

@app.route('/add', methods=['GET','POST'])
def add():
    form = ToDoForm()
    if form.validate_on_submit():
        new_todo = Todos(task=form.task.data,dateAdded=form.dateAdded.data)
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

@app.route('/update/<int:todo_id>', methods=['GET', 'POST'])
def update(todo_id):
    form = ToDoForm()
    todo_to_update = Todos.query.get(todo_id)
    if form.validate_on_submit():
        todo_to_update.task = form.task.data
        db.session.commit()
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.task.data = todo_to_update.task

    return render_template('update.html', form=form)

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo_to_delete = Todos.query.get(todo_id)
    db.session.delete(todo_to_delete)
    db.session.commit()
    return redirect(url_for('index'))
