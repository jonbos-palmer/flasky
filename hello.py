from flask import Flask, request
from flask.helpers import make_response
from flask.templating import render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

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
    user_agent=request.headers.get('User-Agent')
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