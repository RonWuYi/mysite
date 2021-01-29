from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'admin'}
    return '''
<html>
    <head>
        <title>home page</title>
    </head>
    <body>
        <h1>hello, ''' + user['username'] + '''</h1>
    </body>
</html>
'''