from flask import Flask, flash, redirect, render_template, request, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from wtforms import *
from flask_wtf import FlaskForm
from wtforms.widgets import TextArea
from datetime import *
app = Flask(__name__)
Bootstrap(app)
app.secret_key = "yourmum"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
db = SQLAlchemy(app)
class PostForm(FlaskForm):
    username = StringField("Enter your username.")
    content = StringField("LEave us a post here.", widget=TextArea())
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(25))
    username = db.Column(db.String(25))
    password = db.Column(db.String(80))
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25))
    content = db.Column(db.String(144))
    date = db.Column(db.String(10))
    show = db.Column(db.Integer)
@app.route("/", methods=['GET'])
def index():
    all_users = Users.query.all()
    return render_template('index.html', **locals())
@app.route("/posts", methods=['GET'])
def posts():
    all_posts = Posts.query.all()
    return render_template('posts.html', **locals())
@app.errorhandler(404)
def page_not_found(e):
    pass
    #return render_template('404.html'), 404
@app.route("/post", methods=['GET', 'POST'])
def post():
    form = PostForm()
    if request.method == 'POST':
        try:
            new_user = Users(email="hpotter@hogwarts.edu", usernam="hpotter", password="newpassword")
            db.session.add(new_user)
            db.session.commit()
            print("Changed the DB successfully!")
            return index()
        except:
            print("Hmmm...")
            flash("Uh oh, something went wrong.")
    return render_template('post.html', form=form)
@app.route("/post-form", methods=["GET", 'POST'])
def postForm():
    form = PostForm()
    today = str(date.today())
    if form.validate_on_submit():
        try:
            new_post = Posts(username=str(form.username.data), content=str(form.content.data), date=today, show=1)
            db.session.add(new_post)
            db.session.commit()
            print("new post added successufully!")
            return render-template('posts.html')
        except:
            print("Hmmm...")
            flash("Uh oh, somthing wnet wrong.")
    return render_template('post-form.html', form=form)
if __name__ == "__main__":
        app.run(host='0.0.0.0', port=80)
