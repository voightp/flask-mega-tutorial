from flask import render_template
from flask_mail import Message

from app import flask_app, mail
from app.models import User


def send_email(
    subject: str, sender: str, recipients: list[str], text_body: str, html_body: str
) -> None:
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


def send_password_reset_email(user: User):
    token = user.get_reset_password_token()
    send_email(
        "[Microblog] Reset Your Password",
        sender=flask_app.config["ADMINS"][0],
        recipients=[user.email],
        text_body=render_template("email/reset_password.txt", user=user, token=token),
        html_body=render_template("email/reset_password.html", user=user, token=token),
    )
