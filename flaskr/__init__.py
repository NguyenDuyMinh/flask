import os
import random
import datetime
from flask import Flask, render_template
from flaskr.data.models import db
from flaskr.server import auth
from flaskr.server import blog

#db.create_all()

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.register_blueprint(auth.bp)
app.register_blueprint(blog.bp)

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
