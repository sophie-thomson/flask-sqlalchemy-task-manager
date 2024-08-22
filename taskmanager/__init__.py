import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    import env

# Creates an instance of Flask and takes the default name module
app = Flask(__name__)
# takes configuration from the os environment variables in env.py
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE-URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)
# imports the routes.py file from the local taskmanager folder
from taskmanager import routes
