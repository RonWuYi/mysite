from flask import Flask, template_rendered
from contextlib import contextmanager

@contextmanager
def capture_templates(app):
    recorder = []
    def record(sender, template, context, **extra):
        recorder.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield record
    finally:
        template_rendered.disconnect(record, app)
        

if __name__ == '__main__':
    from flask import Flask
    
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return 'index page'
        
    with capture_templates(app) as templates:
        rv = app.test_client().get('/')
        assert rv.status_code == 200
        assert len(templates) == 1
    