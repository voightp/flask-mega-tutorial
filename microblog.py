from app import db, flask_app
from app.models import Post, User


@flask_app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post}
