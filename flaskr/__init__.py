import os
import random
import datetime
from flask import Flask
from flaskr.data.users import db
from flaskr.server import auth

app = Flask(__name__)
app.register_blueprint(auth.bp)
db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
