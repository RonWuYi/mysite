import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

WIN = sys.platform.startswith('win')

if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'
    
    
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:////tmp/test1.db',
        SQLALCHEMY_DATABASE_URI=prefix + os.path.join(app.root_path, 'app.db'),
    )
    # db = SQLAlchemy(app)

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
        
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'hello'
    # db = create_db()
    # db.init_app(app)
    return app

def create_db(app):
    app = create_app()
    db = SQLAlchemy(app)
    db.init_app(app)
    return db

