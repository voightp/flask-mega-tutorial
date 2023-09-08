from flask import render_template

from app import db, flask_app


@flask_app.errorhandler(404)
def not_found_error(error) -> tuple[str, int]:
    return render_template("404.html"), 404


@flask_app.errorhandler(500)
def internal_error(error) -> tuple[str, int]:
    db.session.rollback()
    return render_template("500.html"), 500
