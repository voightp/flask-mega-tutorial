import logging
import os
from logging.handlers import RotatingFileHandler, SMTPHandler

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

flask_app = Flask(__name__)
flask_app.config.from_object(Config)
db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)

login = LoginManager(flask_app)
login.login_view = "login"

mail = Mail(flask_app)

bootstrap = Bootstrap(flask_app)

if not flask_app.debug:
    if flask_app.config["MAIL_SERVER"]:
        auth = None
        if flask_app.config["MAIL_USERNAME"] or flask_app.config["MAIL_PASSWORD"]:
            auth = (
                flask_app.config["MAIL_USERNAME"],
                flask_app.config["MAIL_PASSWORD"],
            )
        secure = None
        if flask_app.config["MAIL_USE_TLS"]:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(flask_app.config["MAIL_SERVER"], flask_app.config["MAIL_PORT"]),
            fromaddr="no-reply@" + flask_app.config["MAIL_SERVER"],
            toaddrs=flask_app.config["ADMINS"],
            subject="Microblog Failure",
            credentials=auth,
            secure=secure,
        )
        mail_handler.setLevel(logging.ERROR)
        flask_app.logger.addHandler(mail_handler)

    if not os.path.exists("logs"):
        os.mkdir("logs")
    file_handler = RotatingFileHandler(
        "logs/microblog.log", maxBytes=10240, backupCount=10
    )
    file_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
        )
    )
    file_handler.setLevel(logging.INFO)
    flask_app.logger.addHandler(file_handler)

    flask_app.logger.setLevel(logging.INFO)
    flask_app.logger.info("Microblog startup")

from app import errors, models, routes  # noqa: F401, E402
