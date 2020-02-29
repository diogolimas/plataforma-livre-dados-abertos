from flask import Flask, request
import threading
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
login = LoginManager(app)
moment = Moment(app)
babel = Babel(app)
bootstrap = Bootstrap(app)

@babel.localeselector
def get_locale():
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    return 'en'

from app import routes, models
