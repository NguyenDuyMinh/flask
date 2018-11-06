from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Demo_wp9@localhost/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Blogs(db.Model):
    __tablename__= 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created = db.Column(db.DateTime, server_default=db.func.now())
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)








