# imports some flask functionality and variables defined in __init__.py file
from flask import render_template
from taskmanager import app, db

# Create a basic app route (or 'view') using / to take you to 'home()' function in base.html
@app.route("/")
def home():
    return render_template("base.html")