import os

from flask import Flask

from .db_sqlalchemy import Session

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'mathapp.sqlite'),
        SQLALCHEMY_DATABASE_URI='sqlite:///instance/mathapp.sqlite',
    )

    @app.teardown_appcontext
    def cleanup(resp_or_exc):
        Session.remove()

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
        return 'Hello, World!'
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    from mathapp.subjects import subjects_view
    app.register_blueprint(subjects_view.bp)
    app.add_url_rule('/', endpoint='index')
        
    return app

