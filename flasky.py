import os

from flask_migrate import Migrate

from app import create_app, db
from hello import User, Role

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

migrate = Migrate(db, app)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)
