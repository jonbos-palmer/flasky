from flask import Flask, request, redirect, session, url_for, flash
from flask.helpers import make_response
from flask.templating import render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
import os


# app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'b quiet'

# extensions
bootstrap = Bootstrap(app)
moment = Moment(app)

# db
basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')

# models


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<Username %r>' % self.username

# forms


class NameForm(FlaskForm):
    name = StringField('What is your name?',
                       validators=[DataRequired()])
    submit = SubmitField('Submit')

# routes

# POST, REDIRECT, GET


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known']=False
        else:
            session['known']=True
        session['name']=form.name.data
        form.name.data=''
        return redirect(url_for('index'))
    return render_template('index.html',form=form, name=session.get('name'), known=session.get('known', False))

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html')


@app.route('/browser')
def get_browser():
    # use requests as if it was a global var
    # django requires passing req to view func
    # neat
    user_agent = request.headers.get('User-Agent')
    return f"{user_agent}"

# return a status


@app.route('/bad')
def get_bad_req():
    return "<h1>Bad request</h1>", 400

# create a response obj and take advantage of built in methods


@app.route('/res-obj')
def get_res_obj():
    response = make_response('this is a response obj')
    response.set_cookie('beach_boy', 'Dennis')
    return response
