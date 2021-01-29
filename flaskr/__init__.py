import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test1.db'
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

