import os
from flask import Flask
from .main.db import Session
from .main.db import override_session

import sys

def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'mathapp.sqlite'),
        SQLALCHEMY_DATABASE_URI='sqlite:///instance/mathapp.sqlite',
        AUTH_SECRET_KEY='auth_placeholder_key',
        FILE_UPLOADS_PATH=os.path.join(app.instance_path, 'uploads'),
    )

    @app.teardown_appcontext
    def cleanup(resp_or_exc):
        Session.remove()

    if test_config is None:
        app.config.from_pyfile('config.py', silent=False)
    else:
        app.config.from_mapping(test_config)
        override_session('sqlite:///instance/test.sqlite')
    

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from mathapp.system.router import auth_web_blueprint
    app.register_blueprint(auth_web_blueprint.bp)
    
    from mathapp.system.router import auth_api_blueprint
    app.register_blueprint(auth_api_blueprint.bp)

    from mathapp.system.router import files_web_blueprint
    app.register_blueprint(files_web_blueprint.bp)

    
    from mathapp.curriculum.router import courses_web_blueprint
    app.register_blueprint(courses_web_blueprint.bp)
    # app.add_url_rule('/', endpoint='index')

    from mathapp.curriculum.router import courses_api_blueprint
    app.register_blueprint(courses_api_blueprint.bp)


    from mathapp.curriculum.router import topics_web_blueprint
    app.register_blueprint(topics_web_blueprint.bp)

    from mathapp.curriculum.router import lessons_web_blueprint
    app.register_blueprint(lessons_web_blueprint.bp)

    from mathapp.curriculum.router import tutorials_web_blueprint
    app.register_blueprint(tutorials_web_blueprint.bp)

    from mathapp.curriculum.router import tutorial_steps_web_blueprint
    app.register_blueprint(tutorial_steps_web_blueprint.bp)

    from mathapp.curriculum.router import exercises_web_blueprint
    app.register_blueprint(exercises_web_blueprint.bp)

    from mathapp.curriculum.router import problem_set_generators_web_blueprint
    app.register_blueprint(problem_set_generators_web_blueprint.bp)

    from mathapp.student.router import course_push_controls_api_blueprint
    app.register_blueprint(course_push_controls_api_blueprint.bp)

    from mathapp.student.router import students_api_blueprint
    app.register_blueprint(students_api_blueprint.bp)

    from mathapp.student.router import student_courses_api_blueprint
    app.register_blueprint(student_courses_api_blueprint.bp)
        
    return app









