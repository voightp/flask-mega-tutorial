from app import flask_app

from flask import render_template


@flask_app.route("/")
@flask_app.route("/index")
def index():
    user = {"username": "Vojtech"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
