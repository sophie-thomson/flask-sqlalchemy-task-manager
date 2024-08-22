# Runs the whole application
import os
from taskmanager import app

# Defines how and when to run the app
if __name__ == "__main__":
    app.run(
        # gets the os environment values defined in the env.py file
        host=os.environ.get("IP"),
        # PORT NEEDS TO BE CONVERTED TO AN INTEGER
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
