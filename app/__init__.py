from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
from .models import Users

def create_app(config_name):
    app = Flask(__name__)
    
    from config import config_options
    app.config.from_object(config_options[config_name])

    from .main import main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')


    db.init_app(app)
    migrate = Migrate(app, db)


    return app


