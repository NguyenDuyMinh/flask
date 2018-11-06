from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort
from flaskr.server.auth import login_required
from flaskr.data.models import Blogs, db


bp = Blueprint('blog', __name__)

@bp.route('/index')
def index():
    posts = Blogs.query.order_by(Blogs.created).all()
    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:  
            blog = Blogs(title = title, body = body, author_id = 1)
            db.session.add(blog)
            db.session.commit() 
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')

def get_post(id, check_author=True):
    post = Blogs.query.filter_by(id=id).first()
    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    return post

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)
    print post
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            blog = Blogs.query.get(id)
            blog.title = title
            blog.body = body
            db.session.commit() 
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    blog = Blogs.query.filter_by(id = id).first()
    db.session.delete(blog)
    db.session.commit() 
    return redirect(url_for('blog.index'))
