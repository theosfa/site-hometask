from flask import Flask, render_template, redirect, url_for, request, session
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from init_weeks.weeks import weeks

app = Flask(__name__)
app.register_blueprint(weeks,url_prefix="/init")
app.secret_key = "LIHBlksdbv7siubkjb7879tn8t5bnBHGbuy5u98u6fGCGFc4d7fCI7gckhgvR58"
app.permanent_session_lifetime = timedelta(days = 365)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    user = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))

    def __init__(self, user, password, email, name, surname):
        self.user = user
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname

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
    session["act_home"] = ""
    session["act_feat"] = ""
    session["act_log"] = ""
    session["sign_url"] = "logging"
    session["sign"] = "Sign in"
    session["page_info"] = "You are on the main page"
    return render_template("index.html", session = session)

@app.route("/view")
def view():
    if users.query.all():
        return render_template("view.html", values = users.query.all())
    else:
        return f"There are no users"

@app.route("/home")
def home():
    if not "user" in session:
        session["logging"] = False
        session["user"] = "no_user"
        session["logged"] = False
    session["act_home"] = "active"
    session["act_feat"] = ""
    session["act_log"] = ""
    session["sign_url"] = "logging"
    session["sign"] = "Sign in"
    session["page_info"] = "You are on the home page"
    return render_template("home.html", session = session)

@app.route("/features")
def features():
    if not "user" in session:
        session["logging"] = False
        session["user"] = "no_user"
        session["logged"] = False
    session["act_home"] = ""
    session["act_feat"] = "active"
    session["act_log"] = ""
    session["sign_url"] = "logging"
    session["sign"] = "Sign in"
    session["page_info"] = "You are on the feature page"
    return render_template("features.html", session = session)

@app.route("/sign_up", methods=["POST", "GET"])
def sign_up():
    if not "user" in session:
        session["logging"] = False
        session["user"] = "no_user"
        session["logged"] = False
    session["act_home"] = ""
    session["act_feat"] = ""
    session["act_log"] = "active"
    session["sign_url"] = "sign_up"
    session["sign"] = "Sign up"
    session["page_info"] = "You are on the sign up page"
    if request.method == "POST":
        user = request.form["usrname"]
        passwd = request.form["passwd"]
        email = request.form["email"]
        # name = request.form["name"]
        # surname = request.form["surname"]
        name = ""
        surname = ""
        found_user = users.query.filter_by(user=user).first()
        if found_user:
            return render_template("sign_up.html",sign_up = False, session = session)
        usr = users(user, passwd, email, name, surname)
        db.session.add(usr)
        db.session.commit()
        session["user"] = user
        session["password"] = passwd
        session["email"] = email
        session["name"] = name
        session["surname"] = surname
        session["logged"] = True
        return redirect(url_for("profile"))
    return render_template("sign_up.html", sign_up = True, session = session)

@app.route("/logging", methods=["POST", "GET"])
def logging():
    if not "user" in session:
        session["logging"] = False
        session["user"] = "no_user"
        session["logged"] = False
    session["act_home"] = ""
    session["act_feat"] = ""
    session["act_log"] = "active"
    session["sign_url"] = "logging"
    session["sign"] = "Sign in"
    session["page_info"] = "You are on the sign in page"
    if request.method == "POST":
        user = request.form["usrname"]
        passwd = request.form["passwd"]
        found_user = users.query.filter_by(user = user).first()
        if found_user:
            session.permanent = True
            session["logged"] = True
            session["user"] = user
            return redirect(url_for("profile"))
        else:
            session["logging"] = False
        if not session["logging"]:
            return render_template("logging.html", session = session)
            session["logging"] = True
    session["logging"] = True
    return render_template("logging.html", session = session)

@app.route("/profile")
def profile():
    if not "user" in session:
        session["logging"] = False
        session["user"] = "no_user"
        session["logged"] = False
    if session["user"] == "no_user":
        return redirect(url_for("logging"))
    session["act_home"] = ""
    session["act_feat"] = ""
    session["act_log"] = "active"
    session["sign"] = "Sign in"
    session["page_info"] = "You are on the profile page"
    return render_template("profile.html", values = users.query.filter_by(user=session["user"]).first(), session = session)

@app.route("/profile/edit")
def edit_profile():
    if not "user" in session:
        session["logging"] = False
        session["user"] = "no_user"
        session["logged"] = False
    if session["user"] == "no_user":
        return redirect(url_for("logging"))
    session["act_home"] = ""
    session["act_feat"] = ""
    session["act_log"] = "active"
    session["sign"] = "Sign in"
    session["page_info"] = "You are on the profile editing page"
    return render_template("edit_profile.html", session = session)

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
