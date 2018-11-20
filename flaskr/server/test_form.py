from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response
)
from flaskr.form.forms import *

bp = Blueprint('test', __name__, url_prefix='/test')

@bp.route('/form', methods=('GET', 'POST'))
def hello():
    form = ReusableForm(request.form)
    
    if request.method == 'POST':
        name=request.form['name']
        password=request.form['password']
        email=request.form['email']

        if form.validate():
            # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('test/form.html', form=form)