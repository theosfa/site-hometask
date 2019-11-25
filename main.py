from flask import Flask, render_template, redirect, url_for, request, session
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from init_lessons.lessons import lessons

app = Flask(__name__)
app.register_blueprint(lessons,url_prefix="/init")
app.secret_key = "LIHBlksdbv7siubkjb7879tn8t5bnBHGbuy5u98u6fGCGFc4d7fCI7gckhgvR58"
app.permanent_session_lifetime = timedelta(years = 1)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///main.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, password, email):
        self.name = name
        self.email = email
        self.password = password

class lessons(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    weekday = db.Column(db.String(100))

    time_1 = db.Column(db.String(100))
    lesson_1 = db.Column(db.String(100))
    hometask_1 = db.Column(db.String(100))
    name_changer_1 = db.Column(db.String(100))

    time_2 = db.Column(db.String(100))
    lesson_2 = db.Column(db.String(100))
    hometask_2 = db.Column(db.String(100))
    name_changer_2 = db.Column(db.String(100))

    time_3 = db.Column(db.String(100))
    lesson_3 = db.Column(db.String(100))
    hometask_3 = db.Column(db.String(100))
    name_changer_3 = db.Column(db.String(100))

    time_4 = db.Column(db.String(100))
    lesson_4 = db.Column(db.String(100))
    hometask_4 = db.Column(db.String(100))
    name_changer_4 = db.Column(db.String(100))

    def __init__(self,weekday):
        self.weekday = weekday

    def lesson1(self, time, lesson, hometask, changer):
        self.time_1 = time
        self.lesson_1 = lesson
        self.hometask_1 = hometask
        self.name_changer_1 = changer

    def lesson2(self, time, lesson, hometask, changer):
        self.time_2 = time
        self.lesson_2 = lesson
        self.hometask_2 = hometask
        self.name_changer_2 = changer

    def lesson3(self, time, lesson, hometask, changer):
        self.time_3 = time
        self.lesson_3 = lesson
        self.hometask_3 = hometask
        self.name_changer_3 = changer

    def lesson4(self, time, lesson, hometask, changer):
        self.time_4 = time
        self.lesson_4 = lesson
        self.hometask_4 = hometask
        self.name_changer_4 = changer


@app.route("/")
def index():
    if not "user" in session:
        session["logging"] = False
        session["user"] = "no_user"
        session["logged"] = False
    logged = session["logged"]
    current_user = session["user"]
    return render_template("index.html", act_home = "", act_feat = "", act_log = "", page_info = "You are on the main page", logged = session["logged"], user_name = session["user"], sign = "Sign in", sign_url = "logging")

@app.route("/view")
def view():
    return render_template("view.html", values = users.query.all())

@app.route("/home")
def home():
    if not "user" in session:
        session["logging"] = False
        session["user"] = "no_user"
        session["logged"] = False
    logged = session["logged"]
    current_user = session["user"]
    return render_template("home.html", act_home = "active", act_feat = "", act_log = "", page_info = "You are on the home page", logged = session["logged"], user_name = session["user"], sign = "Sign in", sign_url = "logging")

@app.route("/features")
def features():
    if not "user" in session:
        session["logging"] = False
        session["user"] = "no_user"
        session["logged"] = False
    logged = session["logged"]
    current_user = session["user"]
    return render_template("features.html", act_home = "", act_feat = "active", act_log = "", page_info = "You are on the feature page", logged = session["logged"], user_name = session["user"], sign = "Sign in", sign_url = "logging")

@app.route("/sign_up", methods=["POST", "GET"])
def sign_up():
    if not "user" in session:
        session["logging"] = False
        session["user"] = "no_user"
        session["logged"] = False
    logging = session["logging"]
    logged = session["logged"]
    if request.method == "POST":
        user = request.form["usrname"]
        passwd = request.form["passwd"]
        email = request.form["email"]
        found_user = users.query.filter_by(name=user).first()
        if found_user:
            return render_template("sign_up.html",sign_up = False, act_home = "", act_feat = "", act_log = "active", page_info = "You are on the sign up page", logged = session["logged"], sign = "Sign in", sign_url = "sign_up")
        usr = users(user, passwd, email)
        numb = numbers(user)
        db.session.add(usr)
        db.session.add(numb)
        db.session.commit()
        session["user"] = user
        session["password"] = passwd
        session["email"] = email
        session["logged"] = True
        return redirect(url_for("profile"))
    return render_template("sign_up.html", act_home = "", act_feat = "", act_log = "active", page_info = "You are on the sign up page" , logged = session["logged"], sign = "Sign up", sign_up = True, sign_url = "sign_up")

@app.route("/logging", methods=["POST", "GET"])
def logging():
    if not "user" in session:
        session["logging"] = False
        session["user"] = "no_user"
        session["logged"] = False
    current_user = session["user"]
    logging = session["logging"]
    logged = session["logged"]
    if request.method == "POST":
        user = request.form["usrname"]
        passwd = request.form["passwd"]
        found_user = users.query.filter_by(name = user).first()
        if found_user:
            session.permanent = True
            session["logged"] = True
            session["user"] = user
            return redirect(url_for("profile"))
        else:
            session["logging"] = False
        if not logging:
            return render_template("logging.html", act_home = "", act_feat = "", act_log = "active", page_info = "You are on the logging page", logging = False, logged = session["logged"], sign = "Sign in", sign_url = "logging")
            session["logging"] = True
    return render_template("logging.html", act_home = "", act_feat = "", act_log = "active", page_info = "You are on the logging page" , logging = True, logged = session["logged"], sign = "Sign in", sign_url = "logging")

@app.route("/profile")
def profile():
    if not "user" in session:
        session["logging"] = False
        session["user"] = "no_user"
        session["logged"] = False
    current_user = session["user"]
    logged = session["logged"]
    if current_user == "no_user":
        return redirect(url_for("logging"))
    else:
        return render_template("profile.html", act_home = "", act_feat = "", act_log = "active", page_info = "You are on the logging page", values = users.query.filter_by(name=session["user"]).first(),user_name = session["user"], logged = session["logged"], sign = "Sign in", sign_url = "logging")

@app.route("/profile/logout")
def logout():
    session["logging"] = False
    session["logged"] = False
    session["user"] = "no_user"
    return redirect(url_for("index"))

if __name__ == "__main__" :
    db.create_all()
    app.run(debug=True)
    # app.run(debug=True, host = "172.105.71.178")
