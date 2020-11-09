from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Todos

class ToDoCheck:
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field):
        all_todos = Todos.query.all()
        for todo in all_todos:
            if todo.task == field.data:
                raise ValidationError(self.message)

#class sortButtons(FlaskForm):
    #srtCmplt = SubmitField('Sort by completed')
    #srtIncmplt = SubmitField('Sort by incompleted')
    #srtOld = SubmitField('Sort Old-New')
    #sortNew SubmitField('Sort New-Old')

class ToDoForm(FlaskForm):
    task = StringField('Task', 
            validators=[DataRequired(), ToDoCheck(message = "Please enter a unique task")])
    dateAdded = DateField('Date to complete')
    submit = SubmitField('Add Todo')

class OrderForm(FlaskForm):
    order = SelectField('Order',
            choices=[('new','Most recent'),
                    ('old', 'Oldest'),
                    ('completed', 'Completed'),
                    ('incompleted', 'Incompleted')
            ])
    submit = SubmitField('Select Order')
