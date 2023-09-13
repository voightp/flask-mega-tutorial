from app import cli, create_app, db
from app.models import Post, User

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context() -> dict[str, object]:
    return {"db": db, "User": User, "Post": Post}


if __name__ == "__main__":
    app.run(debug=True)
