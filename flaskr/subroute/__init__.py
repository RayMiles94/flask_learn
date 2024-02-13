"""  Submodule """
from flask import Blueprint, render_template

app = Blueprint("submodule", __name__, template_folder="templates")


@app.route("/")
def sub_module():
    """Return index html file"""
    return render_template("sub_module.html")


@app.route("/2")
def two():
    """Return page 2"""
    return "page 2"
