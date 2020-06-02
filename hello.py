from flask import Flask, request

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    return f'<h1>Hello {name}!</h1>'

@app.route('/browser')
def get_browser():
    # use requests as if it was a global var
    # django requires passing req to view func
    # neat
    user_agent=request.headers.get('User-Agent')
    return f"{user_agent}"