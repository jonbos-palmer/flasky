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

# models



# forms


# routes

# POST, REDIRECT, GET







# Shell Context
@app.shell_context_processor
def makes_shell_context():
    return dict(db=db, User=User, Role=Role)
