from flask import Flask, render_template

app = Flask(__name__)

name_list = ["ben", "harry", "bob", "jay", "matt", "bill"]

@app.route('/names')
def names():
    return render_template('names.html', names = name_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
