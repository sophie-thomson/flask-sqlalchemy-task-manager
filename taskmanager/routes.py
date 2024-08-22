# imports some flask functionality and variables defined in __init__.py file
from flask import render_template, request, redirect, url_for
from taskmanager import app, db
# imports the classes in order to generate the database
from taskmanager.models import Category, Task


# Create a basic app route (or 'view') using / to take you to 'home()' function in base.html
@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)

# 'get' method will get the form content
# 'post' will add the content to the database
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")
