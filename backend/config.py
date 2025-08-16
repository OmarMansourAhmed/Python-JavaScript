from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# create main Flask application
app = Flask(__name__)

# enable cors to let frontend access backend
CORS(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)