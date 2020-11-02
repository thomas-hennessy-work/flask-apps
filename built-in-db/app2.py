from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:password123@34.105.221.87/steelWorks"

if __name__ == "__main__":
    app.run(debug=True)

print(db)
