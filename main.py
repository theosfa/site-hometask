from flask import Flask, render_template, redirect, url_for, request, session
from datetime import timedelta, datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update
from init_weeks.weeks import weeks

app = Flask(__name__)
app.register_blueprint(weeks,url_prefix="/init")
app.secret_key = "LIHBlksdbv7siubkjb7879tn8t5bnBHGbuy5u98u6fGCGFc4d7fCI7gckhgvR58"


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
    biography = db.Column(db.String(2000))

    def __init__(self, user, password, email, name, surname,biography):
        self.user = user
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname
        self.biography = biography



class lessons(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    weekday = db.Column(db.String(100))
    date = db.Column(db.Date)

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

    def __init__(self,weekday, date):
        self.weekday = weekday
        self.date = date

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
        session["sign_in"] = False
        session["user"] = "no_user"
        session["logged"] = False
    session["act_home"] = ""
    session["act_feat"] = ""
    session["act_log"] = ""
    session["sign_url"] = "sign_in"
    session["sign"] = "Sign in"
    session["page_info"] = "You are on the main page"
    return render_template("index.html", session = session)

@app.route("/users")
def all_users():
    return render_template("all_users.html",values = users.query.all())

@app.route("/view")
def view():
    if users.query.all():
        return render_template("view.html", values = users.query.all())
    else:
        return f"There are no users"

@app.route("/create_today")
def date():
    today = datetime.today().date()
    dates = lessons("Thursday",today)
    db.session.add(dates)
    db.session.commit()
    tommorow = datetime(year = 2019, month = today.month, day = today.day + 1).date()
    dates = lessons("Wensday",tommorow)
    db.session.add(dates)
    db.session.commit()
    return f"{today}, {tommorow}"

@app.route("/today")
def today():
    mylist = []
    today = datetime.today().date()
    mylist.append(today)
    found_date = lessons.query.filter_by(date=datetime.today().date()).first()
    return f"{found_date.weekday}, {today.year}"

@app.route("/tommorow")
def tommorow():
    mylist = []
    today = datetime.today().date()
    tommorow = datetime(year = 2019, month = today.month, day = today.day + 1).date()
    mylist.append(today)
    found_date = lessons.query.filter_by(date=tommorow).first()
    return f"{found_date.weekday}, {tommorow.year}"

@app.route("/home")
def home():
    if not "user" in session:
        session["sign_in"] = False
        session["user"] = "no_user"
        session["logged"] = False
    session["act_home"] = "active"
    session["act_feat"] = ""
    session["act_log"] = ""
    session["sign_url"] = "sign_in"
    session["sign"] = "Sign in"
    session["page_info"] = "You are on the home page"
    return render_template("home.html", session = session)

@app.route("/features")
def features():
    if not "user" in session:
        session["sign_in"] = False
        session["user"] = "no_user"
        session["logged"] = False
    session["act_home"] = ""
    session["act_feat"] = "active"
    session["act_log"] = ""
    session["sign_url"] = "sign_in"
    session["sign"] = "Sign in"
    session["page_info"] = "You are on the feature page"
    return render_template("features.html", session = session)

@app.route("/sign_up", methods=["POST", "GET"])
def sign_up():
    if not "user" in session:
        session["sign_in"] = False
        session["user"] = "no_user"
        session["logged"] = False
    session["act_home"] = ""
    session["act_feat"] = ""
    session["act_log"] = "active"
    session["sign_url"] = "sign_up"
    session["sign"] = "Sign up"
    session["page_info"] = "You are on the sign up page"
    session["sign_up_margin"] = "10px"
    if request.method == "POST":
        user = request.form["usrname"]
        passwd = request.form["passwd"]
        email = request.form["email"]
        name = request.form["name"]
        surname = request.form["surname"]
        biography = ""
        found_user = users.query.filter_by(user=user).first()
        if found_user:
            session["sign_up_margin"] = "0px"
            return render_template("sign_up.html",sign_up = False, session = session)
        usr = users(user, passwd, email, name, surname, biography)
        db.session.add(usr)
        db.session.commit()
        session["user"] = user
        session["logged"] = True
        return redirect(url_for("profile"))
    return render_template("sign_up.html", sign_up = True, session = session)

@app.route("/sign_in", methods=["POST", "GET"])
def sign_in():
    if not "user" in session:
        session["sign_in"] = False
        session["user"] = "no_user"
        session["logged"] = False
    session["act_home"] = ""
    session["act_feat"] = ""
    session["act_log"] = "active"
    session["sign_url"] = "sign_in"
    session["sign"] = "Sign in"
    session["page_info"] = "You are on the sign in page"
    if request.method == "POST":
        user = request.form["usrname"]
        passwd = request.form["passwd"]
        checkbox = request.form["checkbox"]
        session["checkbox"] = checkbox
        found_user = users.query.filter_by(user=user).first()
        if found_user and found_user.password == passwd:
            if checkbox:
                app.permanent_session_lifetime = timedelta(days = 365)
                session.permanent = True
            else:
                session.permanent = False
            session["logged"] = True
            session["user"] = user
            return redirect(url_for("profile"))
        else:
            session["sign_in"] = False
        if not session["sign_in"]:
            return render_template("sign_in.html", session = session)
            session["sign_in"] = True
    session["sign_in"] = True
    return render_template("sign_in.html", session = session)

@app.route("/profile")
def profile():
    if not "user" in session:
        session["sign_in"] = False
        session["logged"] = False
        return redirect(url_for("sign_in"))
    session["act_home"] = ""
    session["act_feat"] = ""
    session["act_log"] = "active"
    session["sign"] = "Sign in"
    session["page_info"] = "You are on the profile page"
    return render_template("profile.html", values = users.query.filter_by(user=session["user"]).first(), session = session)

@app.route("/profile/<user>")
def user_profile(user):
    return render_template("user-profile.html", values = users.query.filter_by(user=user).first(), session = session)

@app.route("/profile/edit", methods= ["POST","GET"])
def edit_profile():
    if not "user" in session:
        session["sign_in"] = False
        session["logged"] = False
        return redirect(url_for("sign_in"))
    session["act_home"] = ""
    session["act_feat"] = ""
    session["act_log"] = "active"
    session["sign"] = "Sign in"
    session["page_info"] = "You are on the profile editing page"
    user = users.query.filter_by(user=session["user"]).first()
    session["row"] = round(len(user.biography) / 79) + 2
    if request.method == "POST" :
        name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]
        biography = request.form["biography"]
        user = users.query.filter_by(user=session["user"]).first()
        session["row"] = round(len(biography) / 79) + 2
        user.name = name
        user.surname = surname
        user.email = email
        user.biography = biography
        db.session.commit()
    return render_template("edit_profile.html", values = users.query.filter_by(user=session["user"]).first(), session = session)

@app.route("/profile/logout")
def logout():
    session["sign_in"] = False
    session["logged"] = False
    session.pop("user")
    return redirect(url_for("index"))

if __name__ == "__main__" :
    db.create_all()
    app.run(debug=True)
    # app.run(debug=True, host = "172.105.71.178")
