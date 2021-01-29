import click

from .__init__ import create_db, create_app
from flask import current_app, g
from flask.cli import with_appcontext

app = create_app()
db = create_db(app)

class User(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f"<User {self.username}>"
    
def init_db():
    db.drop_all()
    db.create_all()
    # db = get_db()

    # with current_app.open_resource('schema.sql') as f:
    #     db.executescript(f.read().decode('utf8'))
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

# def init_app(app):
#     app.teardown_appcontext(close_db)
#     app.cli.add_command(init_db_command)

