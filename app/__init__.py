from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.Config") #instead of the bottom lines

#app.config['SECRET_KEY'] = 'SECRET KEY'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)

from . import models, views

with app.app_context():
    db.create_all()