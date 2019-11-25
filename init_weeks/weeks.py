from flask import Blueprint, render_template

weeks = Blueprint("weeks", __name__, static_folder="static",template_folder="templates")

@weeks.route("/first_week")
def first_week():
    return render_template("test.html")

@weeks.route("/second_week")
def second_week():
    return render_template("test.html")

@weeks.route("/third_week")
def third_week():
    return render_template("test.html")

@weeks.route("/fourth_week")
def fourth_week():
    return render_template("test.html")
