from flask import Flask, request
from flask.helpers import make_response

app = Flask(__name__)

@app.route('/dynamic/<name>')
def index(name):
    return f'<h1>Hello {name}!</h1>'

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