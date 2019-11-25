from flask import Blueprint, render_template

lessons = Blueprint("lessons", __name__, static_folder="static",template_folder="templates")

@lessons.route("/first_week")
def first_week():
    return render_template("test.html")

@lessons.route("/second_week")
def second_week():
    return render_template("test.html")

@lessons.route("/third_week")
def third_week():
    return render_template("test.html")

@lessons.route("/fourth_week")
def fourth_week():
    return render_template("test.html")
