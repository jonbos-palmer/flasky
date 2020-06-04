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
from flask_migrate import Migrate
import os
from flask_mail import Mail, Message
from threading import Thread
# app
app = Flask(__name__)



# extensions
bootstrap = Bootstrap(app)
moment = Moment(app)

# db
basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy(app)
migrate = Migrate(app, db)


#mail

mail = Mail(app)

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender = app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template+'.txt', **kwargs)
    msg.html = render_template(template+'.html', **kwargs)
    thr = Thread(target-send_async_email, args=[app, msg])
    thr.start()
    return thr
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


# routes

# POST, REDIRECT, GET







# Shell Context
@app.shell_context_processor
def makes_shell_context():
    return dict(db=db, User=User, Role=Role)
