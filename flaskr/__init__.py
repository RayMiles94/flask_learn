#!/usr/bin/env python
"""Module flask."""

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Return index html file"""
    return render_template("index.html")


@app.route("/submit", methods=["GET"])
def form_submit():
    "form veiw"
    if request.method == "GET":
        datas = request.form
        print(datas)
        return "Okay"

    return "Not Okay"


if __name__ == "__main__":
    app.run(port=4900, debug=True)
