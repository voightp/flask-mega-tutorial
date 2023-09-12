from app import app, cli, db  # noqa: F401
from app.models import Post, User


@app.shell_context_processor
def make_shell_context() -> dict[str, object]:
    return {"db": db, "User": User, "Post": Post}


if __name__ == "__main__":
    app.run(debug=True)
