import os
import random
import datetime

from flask import Flask
from flask_mysqldb import MySQL
#from . import db
from . import auth
from . import blog


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.permanent_session_lifetime = datetime.timedelta(seconds=360)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') # or \ 'e5ac358c-f0bf-11e5-9e39-d3b532c10a28'
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    #with app.app_context():
    #    db.init_db()
        
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app