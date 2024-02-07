from flask import render_template, request, Blueprint, redirect, url_for
from flaskblog.models import Post
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route("/")
def startup():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    return render_template('startup.html')

@main.route("/home")
@login_required
def home():
    page = request.args.get('page',1, type=int)
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts, title = 'Home')


@main.route("/about")
def about():
    return render_template('about.html', title = 'About')

