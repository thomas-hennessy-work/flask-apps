from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField, IntegerField, DecimalField, SelectField, DateField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    given_date = DateField('A date you like')
    given_int = IntegerField('A special int')
    given_dec = DecimalField('A special decimal')
    president = SelectField('Presidential Candidate', choices=[('Rep', 'Trump'), ('Dem', 'Biden')])
    #language = SelectField('Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    submit = SubmitField('Add Name')


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = "Please supply first and last name"
        else:
            return 'thank you '+first_name+' '+last_name+' for your information'

    return render_template('home.html', form=form, message=error)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
