#!/usr/bin/env python
"""Module flask."""

from flask import Flask, render_template, request
from flaskr.db import db_session, init_db
from flaskr.models import User

app = Flask(__name__)
init_db()


@app.route("/")
def hello_world():
    """Return index html file"""
    print(User.query.all())
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def form_submit():
    "form veiw"
    if request.method == "POST":
        print(User.query.all())
        datas = request.form
        user_data = User(datas["email1"], datas["password1"])
        db_session.add(user_data)
        db_session.commit()
        return "Okay"
    return "Not Okay"


@app.teardown_appcontext
def shutdown_session(exception=None):
    """ Shitdown session """
    db_session.remove()


if __name__ == "__main__":
    app.run(port=4900, debug=True)
