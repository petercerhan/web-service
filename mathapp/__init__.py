import os
from flask import Flask
from .db import Session

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
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    from mathapp.flask import courses_web_blueprint
    app.register_blueprint(courses_web_blueprint.bp)
    app.add_url_rule('/', endpoint='index')

    from mathapp.flask import lessons_web_blueprint
    app.register_blueprint(lessons_web_blueprint.bp)
        
    return app

