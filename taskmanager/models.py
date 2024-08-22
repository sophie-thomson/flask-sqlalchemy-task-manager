# Defines the data models (tables) and database
# Import db variable defined in __init__.py file
from taskmanager import db


class Category(db.Model):
    # schema for the Category model
    # Each row on the table has a unique id as the first column
    # Parameters inside () define data type and if primary key
    # Is a 'primary_key' as not taken from any other table
    id = db.Column(db.Integer, primary_key=True)
    # parameters set data type to 'string' with max 25 characters
    # Must be unique category (not already exist), and is a 'required' field
    # (can't be empty / blank)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    # db.relationship() not visible as a 'column' - is a link reference to the
    # 'one to many' ForeignKey in the Task table. "Task" targets the Task table 
    # 'backref' establishes bi-directional relationship between the two tables.
    # 'cascade="all, delete" means that all associated tasks will be deleted
    # lazy=True means when we query database for categories can simultaniously identify any task linked to the categories
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)


    # Create function called __repr__() to represent class objects as a string
    def __repr__(self):
        # represents itself as a string
        return self.category_name



class Task(db.Model):
    # schema for the Task model
    # Each row on the table has a unique id as the first column
    # Is a 'primary_key' as not taken from any other table
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    # Can also use db. DateTime or db.Time if you need to add a time
    due_date = db.Column(db.Date, nullable=False)
    # category_id is taken from category table so is a 'ForeignKey'
    # ondelete="CASCADE" indicates a 'one to many' relationship where
    # one category can be assigned to many different tasks. If cat deleted, then all tasks 
    # under that category are also deleted (cascade effect)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # represents itself as a string
        # Uses placeholders of {0}, {1}, and {2}
        # Python .format method tells prog what data to put in each placeholder
        return "#{0} - Task: {1}  |  Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )