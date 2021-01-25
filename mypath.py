from flask_wtf import FlaskForm
from wtforms import StringField

from wtforms.validators import DataRequired

from flask import Flask, request

app = Flask(__name__)
class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    
@app.route('/')
def index():
    return 'index page'
    
@app.route('/log', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
    <form method="POST" action="/">
    {{ form.csrf_token }}
    {{ form.name.label }} {{ form.name(size=20) }}
    <input type="submit" value="Go">
</form>
    '''
    else:
        return 'post page'
    
    
if __name__ == '__main__':
    import os
    app.run()
