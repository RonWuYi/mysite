import os

from flask_wtf import FlaskForm
from wtforms import StringField
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms.validators import DataRequired

from flask import Flask, request,redirect, url_for, render_template
from wtforms import Form, BooleanField, TextField, PasswordField, validators

class RegistrationForm(Form):
    username = TextField('username', [validators.Length(min=4, max=25)])
    email = TextField('email address', [validators.Length(min=6, max=35)])
    
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
        ])
    confirm = PasswordField('Repeate Password')
    accept_tos = BooleanField('I accept the TOS', [validators.Required()])


app = Flask(__name__)

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    
@app.route('/')
def index():
    return 'index page'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, 
                    form.email.data,
                    form.password.data)
        db_session.add(user)
        
        
        
# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.form.validate_on_submit():
#         f = request.form.photo.data
#         filename = secure_filename(f.filename)
#         f.save(os.path.join(
#             app.instance_path, 'photos', filename
#         ))
        
#         return redirect(url_for('index'))
    
#     return render_template('upload.html', form=form)
    
# @app.route('/log', methods=['GET', 'POST'])
# def login():
#     if request.method == 'GET':
#         return '''
#     <form method="POST" action="/">
#     {{ form.csrf_token }}
#     {{ form.name.label }} {{ form.name(size=20) }}
#     <input type="submit" value="Go">
# </form>
#     '''
#     else:
#         return 'post page'
    
    
# if __name__ == '__main__':
#     import os
#     app.run()
