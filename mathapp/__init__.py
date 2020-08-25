import os
from flask import Flask
from .sqlalchemy.db import Session
from .sqlalchemy.db import override_session

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
        override_session('sqlite:///instance/test.sqlite')
    

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from mathapp.flask import auth_web_blueprint
    app.register_blueprint(auth_web_blueprint.bp)
    
    from mathapp.flask import courses_web_blueprint
    app.register_blueprint(courses_web_blueprint.bp)
    app.add_url_rule('/', endpoint='index')

    from mathapp.flask import lessons_web_blueprint
    app.register_blueprint(lessons_web_blueprint.bp)
        
    return app

