import click
from flask import current_app, g, Flask
from flask.cli import with_appcontext
from flask_mysqldb import MySQL

def get_db():
    if 'db' not in g:
        app = Flask(__name__)
        app.config['MYSQL_USER'] = 'root'
        app.config['MYSQL_PASSWORD'] = 'Demo_wp9'
        app.config['MYSQL_DB'] = 'testdb'
        app.config['MYSQL_HOST'] = 'localhost'
        mysql = MySQL(app)
        g.db = mysql.connect()
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
