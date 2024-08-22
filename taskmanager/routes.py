# imports some flask functionality and variables defined in __init__.py file
from flask import render_template
from taskmanager import app, db
# imports the classes in order to generate the database
from taskmanager.models import Category, Task

# Create a basic app route (or 'view') using / to take you to 'home()' function in base.html
@app.route("/")
def home():
    return render_template("tasks.html")