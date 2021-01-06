from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

def create_app():
    app = Flask(__name__)

    # 블루프린트 적용
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app