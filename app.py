import os
import sys

# from sqlite3 import IntegrityError
from flask import Flask, render_template, redirect, url_for, request
from flask_login import login_required, current_user, login_user, logout_user

from appcopy3 import db, UserModel, login_manager

WIN = sys.platform.startswith('win')

if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'dev'

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/hello')
def hello():
    return redirect(url_for('index'))

@app.route('/hello1')
def hello1():
    return 'hello1 page'

@app.route('/')
def index():
    return 'index page'

@login_required
@app.route('/test')
def test():
    return redirect(url_for('hello1'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blogs'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        user = UserModel.query.filter_by(email=email).first()
        
        if user is not None and user.check_password(request.form.get('password')):
            login_user(user)
            return redirect(url_for('blogs'))
        
    return render_template('login.html')
        
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('blogs'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        
        if UserModel.query.filter_by(email=email).first():
            return ('Email already Present')
        
        user = UserModel(email=email, username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@login_required
@app.route('/blogs')    
def blogs():
    return render_template('blog.html')
    
if __name__ == '__main__':
    app.run(host='localhost', port=5001)
# db = SQLAlchemy(app)

# login_manager = flask_login.LoginManager()

# login_manager.init_app(app)

# class User(db.Model):
#     __tablename__ = 'user'
    
#     email = db.Column(db.String, primary_key=True)
#     password = db.Column(db.String)
#     authenticated = db.Column(db.Boolean)
# class Username(flask_login.UserMixin):
#     pass

# @login_manager.user_loader
# def user_loader(email):
#     if email not in users:
#         return
    
#     user = Username()
#     user.id = email
#     return user

# @login_manager.request_loader
# def request_loader(request):
#     email = request.form.get('email')
#     if email not in users:
#         return
#     user = Username()
#     user.id = email
    
#     user.is_authenticated = request.form['password'] == users[email]['password']
    
#     return user

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if flask.request.method == 'GET':
#         return '''
#                   <form action='login' method='POST'>
#                 <input type='text' name='email' id='email' placeholder='email'/>
#                 <input type='password' name='password' id='password' placeholder='password'/>
#                 <input type='submit' name='submit'/>
#                 </form>
#                 '''
#     email = flask.request.form.get['email']
#     if request.form['password'] == users[email]['password']:
#         user = Username()
#         user.id = email
#         flask_login.login_user(user)
#         return flask.redirect(flask.url_for('protected'))
    
#     return 'Bad login'
    
# @app.route('/protected')
# @flask_login.login_required
# def protected():
#     return 'Logged in as: ' + flask_login.current_user.id

# @app.route('/logout')
# def logout():
#     flask_login.logout_user()
#     return 'Logged out'

# @login_manager.unauthorized_handler
# def unauthorized_handler():
#     return 'Unauthorized'
# class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     name = db.Column(db.String(20), unique=True)  # 名字
#     username = db.Column(db.String(20))
#     password = db.Column(db.String(128))
# class Movie(db.Model):  # 表名将会是 movie
#     id = db.Column(db.Integer, primary_key=True)  # 主键
#     title = db.Column(db.String(60), unique=True)  # 电影标题
#     year = db.Column(db.String(4))  # 电影年份

# @app.cli.command()
# @click.option('--drop', is_flag=True, help='Create db after drop.')
# def initdb(drop):
#     """
#     Initialize the database.
#     """
#     if drop:
#         db.drop_all()
#     db.create_all()
#     click.echo('Initialized databases.')

# @app.cli.command()
# def forge():
#     """Generate fake data."""
#     db.create_all()
#     name = 'test'
#     movies = [
#     {'title': 'My Neighbor Totoro', 'year': '1988'},
#     {'title': 'Dead Poets Society', 'year': '1989'},
#     {'title': 'A Perfect World', 'year': '1993'},
#     {'title': 'Leon', 'year': '1994'},
#     {'title': 'Mahjong', 'year': '1996'},
#     {'title': 'Swallowtail Butterfly', 'year': '1996'},
#     {'title': 'King of Comedy', 'year': '1999'},
#     {'title': 'Devils on the Doorstep', 'year': '1999'},
#     {'title': 'WALL-E', 'year': '2008'},
#     {'title': 'The Pork of Music', 'year': '2012'},
# ]    

#     user = User(name=name)
#     db.session.add(user)
#     for m in movies:
#         movie =Movie(title=m['title'], year=m['year'])
#         db.session.add(movie)
        
#     db.session.commit()
#     click.echo('Done.')

# @app.errorhandler(404)
# def page_not_found(e):
#     user = User.query.first()
#     return render_template('404.html'), 404
    
# @app.context_processor
# def inject_user():
#     user = User.query.first()
#     return dict(user=user)
    
# # @app.route('/hello', methods=['GET', 'POST'])
# # @app.route('/home', methods=['GET', 'POST'])
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         title = request.form.get('title')
#         year = request.form.get('year')
        
#         if not title or not year or len(year) > 4 or len(title) > 50:
#             flash('Invalid input.')
#             return redirect(url_for('index'))
        
#         movie = Movie(title=title, year=year)
#         db.session.add(movie)
#         try:
#             db.session.commit()
#             flash('Item created.')
#             return redirect(url_for('index'))
#         except (IntegrityError) as err:            # flash(e)
#             db.session.rollback()
#             flask.abort(409, err.orig)
#             # return redirect(url_for('index'))
#         except Exception as e:
#             # flash(e)
#             db.session.rollback()
#             flask.abort(500, e)
        
#     movies = Movie.query.all()
#     return render_template('index.html', movies=movies)
