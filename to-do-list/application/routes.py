from application import app, db
from application.models import listItems

@app.route('/')
def index():
    all_tasks = listItems.query.all()
    {% for task in all_tasks %}
    <p> {{task}} </p>
    {% endfor %}
