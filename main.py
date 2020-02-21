from flask import Flask, render_template, redirect, url_for, request, session
from datetime import timedelta, datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update
from init_weeks.weeks import weeks
import random as rand
import requests
import json
import findWeekNumber as fwn

url = 'https://journal.bsuir.by/api/v1/studentGroup/schedule?studentGroup=921701'

r = requests.get(url)

def what_today_dz():
    global subjects
    global view_dz1
    global view_dz2
    global view_dz3
    global view_dz4
    today_day = datetime.today().weekday()
    if today_day == 0:
        session["dz1"] = subjects["mon"][0]
        session["dz2"] = subjects["mon"][1]
        session["dz3"] = subjects["mon"][2]
        session["dz4"] = subjects["mon"][3]
        session["t_dz1"] = type_mon[0]
        session["t_dz2"] = type_mon[1]
        session["t_dz3"] = type_mon[2]
        session["t_dz4"] = type_mon[3]
    if today_day == 1:
        session["dz1"] = subjects["tue"][0]
        session["dz2"] = subjects["tue"][1]
        session["dz3"] = subjects["tue"][2]
        session["dz4"] = subjects["tue"][3]
        session["t_dz1"] = type_tue[0]
        session["t_dz2"] = type_tue[1]
        session["t_dz3"] = type_tue[2]
        session["t_dz4"] = type_tue[3]
    if today_day == 2:
        session["dz1"] = subjects["wen"][0]
        session["dz2"] = subjects["wen"][1]
        session["dz3"] = subjects["wen"][2]
        session["dz4"] = subjects["wen"][3]
        session["t_dz1"] = type_wen[0]
        session["t_dz2"] = type_wen[1]
        session["t_dz3"] = type_wen[2]
        session["t_dz4"] = type_wen[3]
    if today_day == 3:
        session["dz1"] = subjects["thu"][0]
        session["dz2"] = subjects["thu"][1]
        session["dz3"] = subjects["thu"][2]
        session["dz4"] = subjects["thu"][3]
        session["t_dz1"] = type_thu[0]
        session["t_dz2"] = type_thu[1]
        session["t_dz3"] = type_thu[2]
        session["t_dz4"] = type_thu[3]
    if today_day == 4:
        session["dz1"] = subjects["fri"][0]
        session["dz2"] = subjects["fri"][1]
        session["dz3"] = subjects["fri"][2]
        session["dz4"] = subjects["fri"][3]
        session["t_dz1"] = type_fri[0]
        session["t_dz2"] = type_fri[1]
        session["t_dz3"] = type_fri[2]
        session["t_dz4"] = type_fri[3]
    if today_day == 5:
        session["dz1"] = ""
        session["dz2"] = ""
        session["dz3"] = ""
        session["dz4"] = ""
        session["t_dz1"] = "ЛК"
        session["t_dz2"] = "ЛК"
        session["t_dz3"] = "ЛК"
        session["t_dz4"] = "ЛК"
    if today_day == 6:
        session["dz1"] = ""
        session["dz2"] = ""
        session["dz3"] = ""
        session["dz4"] = ""
        session["t_dz1"] = "ЛК"
        session["t_dz2"] = "ЛК"
        session["t_dz3"] = "ЛК"
        session["t_dz4"] = "ЛК"
    if session["t_dz1"] == "ЛК":
        view_dz1 = False
    if session["t_dz2"] == "ЛК":
        view_dz2 = False
    if session["t_dz3"] == "ЛК":
        view_dz3 = False
    if session["t_dz4"] == "ЛК":
        view_dz4 = False




subjects = {
    "mon" : ["","","","","","","",""],
    "tue" : ["","","","","","","",""],
    "wen" : ["","","","","","","",""],
    "thu" : ["","","","","","","",""],
    "fri" : ["","","","","","","",""]
}
auditories = {
    "mon" : ["","","","","","","",""],
    "tue" : ["","","","","","","",""],
    "wen" : ["","","","","","","",""],
    "thu" : ["","","","","","","",""],
    "fri" : ["","","","","","","",""]
}
employees = {
    "mon" : ["","","","","","","",""],
    "tue" : ["","","","","","","",""],
    "wen" : ["","","","","","","",""],
    "thu" : ["","","","","","","",""],
    "fri" : ["","","","","","","",""]
}
type_mon = ["","","","","","",""]
type_tue = ["","","","","","",""]
type_wen = ["","","","","","",""]
type_thu = ["","","","","","",""]
type_fri = ["","","","","","",""]
weekNumber = fwn.weekNumber()
def check_schedule():
    numsub = 0
    subGroup = 1
    global r
    for i in r.json()["schedules"]:
        if i["weekDay"] == "Понедельник":
            for j in i["schedule"]:
                for n in j["weekNumber"]:
                    if n == weekNumber:
                        if j["numSubgroup"] == subGroup or j["numSubgroup"] == 0:
                            if j["subject"] == subjects["mon"][numsub-1] and j["lessonType"] == type_mon[numsub-1]:
                                numsub = numsub - 1
                            subjects["mon"][numsub] = j["subject"]
                            auditories["mon"][numsub] = j["auditory"]
                            for g in j["employee"]:
                                employees["mon"][numsub] = str(g["lastName"]) + " " + str(g["firstName"])[0] + "." + str(g["middleName"])[0] + "."
                                if g["lastName"] == "Карпик" and subGroup != 1:
                                    numsub = numsub - 1
                                elif g["lastName"] == "Синкевич" and subGroup != 2:
                                    numsub = numsub - 1
                            type_mon[numsub] = j["lessonType"]
                            numsub = numsub + 1
        numsub = 0
        if i["weekDay"] == "Вторник":
            for j in i["schedule"]:
                for n in j["weekNumber"]:
                    if n == weekNumber:
                        if j["numSubgroup"] == subGroup or j["numSubgroup"] == 0:
                            if j["subject"] == subjects["tue"][numsub-1] and j["lessonType"] == type_tue[numsub-1]:
                                numsub = numsub - 1
                            subjects["tue"][numsub] = j["subject"]
                            auditories["tue"][numsub] = j["auditory"]
                            for g in j["employee"]:
                                employees["tue"][numsub] = str(g["lastName"]) + " " + str(g["firstName"])[0] + "." + str(g["middleName"])[0] + "."
                                if g["lastName"] == "Карпик" and subGroup != 1:
                                    numsub = numsub - 1
                                elif g["lastName"] == "Синкевич" and subGroup != 2:
                                    numsub = numsub - 1
                            type_tue[numsub] = j["lessonType"]
                            numsub = numsub + 1
        numsub = 0
        if i["weekDay"] == "Среда":
            for j in i["schedule"]:
                for n in j["weekNumber"]:
                    if n == weekNumber:
                        if j["numSubgroup"] == subGroup or j["numSubgroup"] == 0:
                            if j["subject"] == subjects["wen"][numsub-1] and j["lessonType"] == type_wen[numsub-1]:
                                numsub = numsub - 1
                            subjects["wen"][numsub] = j["subject"]
                            auditories["wen"][numsub] = j["auditory"]
                            for g in j["employee"]:
                                employees["wen"][numsub] = str(g["lastName"]) + " " + str(g["firstName"])[0] + "." + str(g["middleName"])[0] + "."
                                if g["lastName"] == "Карпик" and subGroup != 1:
                                    numsub = numsub - 1
                                elif g["lastName"] == "Синкевич" and subGroup != 2:
                                    numsub = numsub - 1
                            type_wen[numsub] = j["lessonType"]
                            numsub = numsub + 1
        numsub = 0
        if i["weekDay"] == "Четверг":
            for j in i["schedule"]:
                for n in j["weekNumber"]:
                    if n == weekNumber:
                        if j["numSubgroup"] == subGroup or j["numSubgroup"] == 0:
                            if j["subject"] == subjects["thu"][numsub-1] and j["lessonType"] == type_thu[numsub-1]:
                                numsub = numsub - 1
                            subjects["thu"][numsub] = j["subject"]
                            auditories["thu"][numsub] = j["auditory"]
                            for g in j["employee"]:
                                employees["thu"][numsub] = str(g["lastName"]) + " " + str(g["firstName"])[0] + "." + str(g["middleName"])[0] + "."
                                if g["lastName"] == "Карпик" and subGroup != 1:
                                    numsub = numsub - 1
                                elif g["lastName"] == "Синкевич" and subGroup != 2:
                                    numsub = numsub - 1
                            type_thu[numsub] = j["lessonType"]
                            numsub = numsub + 1
        numsub = 0
        if i["weekDay"] == "Пятница":
            for j in i["schedule"]:
                for n in j["weekNumber"]:
                    if n == weekNumber:
                        if j["numSubgroup"] == subGroup or j["numSubgroup"] == 0:
                            if j["subject"] == subjects["fri"][numsub-1] and j["lessonType"] == type_fri[numsub-1]:
                                numsub = numsub - 1
                            subjects["fri"][numsub] = j["subject"]
                            auditories["fri"][numsub] = j["auditory"]
                            for g in j["employee"]:
                                employees["fri"][numsub] = str(g["lastName"]) + " " + str(g["firstName"])[0] + "." + str(g["middleName"])[0] + "."
                                if g["lastName"] == "Карпик" and subGroup != 1:
                                    numsub = numsub - 1
                                elif g["lastName"] == "Синкевич" and subGroup != 2:
                                    numsub = numsub - 1
                            type_fri[numsub] = j["lessonType"]
                            numsub = numsub + 1
        numsub = 0


# what_today_dz()


app = Flask(__name__)
app.register_blueprint(weeks,url_prefix="/init")
app.secret_key = "LIHBlksdbv7siubkjb7879tn8t5bnBHGbuy5u98u6fGCGFc4d7fCI7gckhgvR58"
view_dz1 = True
view_dz2 = True
view_dz3 = True
view_dz4 = True


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
@app.route("/info-page")
def index():
    global view_dz1
    global view_dz2
    global view_dz3
    global view_dz4
    session["view_dz1"] = view_dz1
    session["view_dz2"] = view_dz2
    session["view_dz3"] = view_dz3
    session["view_dz4"] = view_dz4
    global subjects
    if not "color" in session:
        session["txtcolor"] = "black"
        session["bgcolor"] = "white"
        session["color"] = "White"
    session["onpage"] = "index"
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
    return render_template("index.html", session = session, view1 = view_dz1, view2 = view_dz2, view3 = view_dz3, view4 = view_dz4)

@app.route("/users")
def all_users():
    return render_template("all_users.html",values = users.query.all())

# @app.route("/view")
# def view():
#     if users.query.all():
#         return render_template("view.html", values = users.query.all())
#     else:
#         return f"There are no users"

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

@app.route("/schedule", methods=["post","get"])
def home():
    global view_dz1
    global view_dz2
    global view_dz3
    global view_dz4
    session["view_dz1"] = view_dz1
    session["view_dz2"] = view_dz2
    session["view_dz3"] = view_dz3
    session["view_dz4"] = view_dz4
    global subjects
    global employees
    global auditories
    check_schedule()
    session["onpage"] = "home"
    if  not "view_dz1" in session:
        session["view_dz1"] = view_dz1
    if not "view_dz2" in session:
        session["view_dz2"] = view_dz2
    if not "view_dz3" in session:
        session["view_dz3"] = view_dz3
    if not "view_dz4" in session:
        session["view_dz4"] = view_dz4
    if not "color" in session:
        session["txtcolor"] = "black"
        session["bgcolor"] = "white"
        session["color"] = "White"
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
    if request.method == "POST":
        view_dz1 = True
        view_dz2 = True
        view_dz3 = True
        view_dz4 = True
        session["view_dz1"] = view_dz1
        session["view_dz2"] = view_dz2
        session["view_dz3"] = view_dz3
        session["view_dz4"] = view_dz4
    return render_template("schedule.html", session = session, view1 = view_dz1, view2 = view_dz2, view3 = view_dz3, view4 = view_dz4, type_mon = type_mon, type_tue = type_tue, type_wen = type_wen, type_thu = type_thu, type_fri = type_fri, subjects = subjects, employees = employees, auditories = auditories)

@app.route("/home-edit", methods=["post","get"])
def features():
    session["onpage"] = "features"
    if not "color" in session:
        session["txtcolor"] = "black"
        session["bgcolor"] = "white"
        session["color"] = "White"
    if not "user" in session:
        session["sign_in"] = False
        session["user"] = "no_user"
        session["logged"] = False
    gen_number = {}
    number_of_numbers = 5
    session["act_home"] = ""
    session["act_feat"] = "active"
    session["act_log"] = ""
    session["sign_url"] = "sign_in"
    session["sign"] = "Sign in"
    session["page_info"] = "You are on the feature page"
    if request.method == "POST":
        for i in range(number_of_numbers):
            gen_number[i] = rand.randint(1, 465)
    return render_template("hometask-edit.html", session = session, generated_number = gen_number)

@app.route("/dz1", methods=["POST","GET"])
def dz1():
    global view_dz1
    global view_dz2
    global view_dz3
    global view_dz4
    session["view_dz1"] = view_dz1
    session["view_dz2"] = view_dz2
    session["view_dz3"] = view_dz3
    session["view_dz4"] = view_dz4
    session["onpage"] = "dz1"
    if not "color" in session:
        session["txtcolor"] = "black"
        session["bgcolor"] = "white"
        session["color"] = "White"
    session["view_dz1"] = view_dz1
    if request.method == "POST":
        view_dz1 = False
        session["view_dz1"] = view_dz1
        return redirect(url_for("home"))
    return render_template("dz1.html",session = session, view1 = view_dz1, view2 = view_dz2, view3 = view_dz3, view4 = view_dz4)

@app.route("/dz2", methods=["POST","GET"])
def dz2():
    global view_dz1
    global view_dz2
    global view_dz3
    global view_dz4
    session["view_dz1"] = view_dz1
    session["view_dz2"] = view_dz2
    session["view_dz3"] = view_dz3
    session["view_dz4"] = view_dz4
    session["onpage"] = "dz2"
    if not "color" in session:
        session["txtcolor"] = "black"
        session["bgcolor"] = "white"
        session["color"] = "White"
    session["view_dz2"] = view_dz2
    if request.method == "POST":
        view_dz2 = False
        session["view_dz2"] = view_dz2
        return redirect(url_for("home"))
    return render_template("dz2.html",session = session, view1 = view_dz1, view2 = view_dz2, view3 = view_dz3, view4 = view_dz4)

@app.route("/dz3", methods=["POST","GET"])
def dz3():
    global view_dz1
    global view_dz2
    global view_dz3
    global view_dz4
    session["view_dz1"] = view_dz1
    session["view_dz2"] = view_dz2
    session["view_dz3"] = view_dz3
    session["view_dz4"] = view_dz4
    session["onpage"] = "dz3"
    if not "color" in session:
        session["txtcolor"] = "black"
        session["bgcolor"] = "white"
        session["color"] = "White"
    session["view_dz3"] = view_dz3
    if request.method == "POST":
        view_dz3 = False
        session["view_dz3"] = view_dz3
        return redirect(url_for("home"))
    return render_template("dz3.html",session = session, view1 = view_dz1, view2 = view_dz2, view3 = view_dz3, view4 = view_dz4)

@app.route("/dz4", methods=["POST","GET"])
def dz4():
    global view_dz1
    global view_dz2
    global view_dz3
    global view_dz4
    session["view_dz1"] = view_dz1
    session["view_dz2"] = view_dz2
    session["view_dz3"] = view_dz3
    session["view_dz4"] = view_dz4
    session["onpage"] = "dz4"
    session["view_dz4"] = view_dz4
    if not "color" in session:
        session["txtcolor"] = "black"
        session["bgcolor"] = "white"
        session["color"] = "White"
    if request.method == "POST":
        view_dz4 = False
        session["view_dz4"] = view_dz4
        return redirect(url_for("home"))
    return render_template("dz4.html",session = session, view1 = view_dz1, view2 = view_dz2, view3 = view_dz3, view4 = view_dz4)

@app.route("/sign_up", methods=["POST", "GET"])
def sign_up():
    global view_dz1
    global view_dz2
    global view_dz3
    global view_dz4
    session["view_dz1"] = view_dz1
    session["view_dz2"] = view_dz2
    session["view_dz3"] = view_dz3
    session["view_dz4"] = view_dz4
    session["onpage"] = "sign_up"
    if  not "view_dz1" in session:
        session["view_dz1"] = view_dz1
    if not "view_dz2" in session:
        session["view_dz2"] = view_dz2
    if not "view_dz3" in session:
        session["view_dz3"] = view_dz3
    if not "view_dz4" in session:
        session["view_dz4"] = view_dz4
    if not "color" in session:
        session["txtcolor"] = "black"
        session["bgcolor"] = "white"
        session["color"] = "White"
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
            return render_template("sign_up.html",sign_up = False, session = session, view1 = view_dz1, view2 = view_dz2, view3 = view_dz3, view4 = view_dz4)
        usr = users(user, passwd, email, name, surname, biography)
        db.session.add(usr)
        db.session.commit()
        session["user"] = user
        session["logged"] = True
        return redirect(url_for("profile"))
    return render_template("sign_up.html", sign_up = True, session = session, view1 = view_dz1, view2 = view_dz2, view3 = view_dz3, view4 = view_dz4)

@app.route("/sign_in", methods=["POST", "GET"])
def sign_in():
    global view_dz1
    global view_dz2
    global view_dz3
    global view_dz4
    session["view_dz1"] = view_dz1
    session["view_dz2"] = view_dz2
    session["view_dz3"] = view_dz3
    session["view_dz4"] = view_dz4
    session["onpage"] = "sign_in"
    if  not "view_dz1" in session:
        session["view_dz1"] = view_dz1
    if not "view_dz2" in session:
        session["view_dz2"] = view_dz2
    if not "view_dz3" in session:
        session["view_dz3"] = view_dz3
    if not "view_dz4" in session:
        session["view_dz4"] = view_dz4
    if not "color" in session:
        session["txtcolor"] = "black"
        session["bgcolor"] = "white"
        session["color"] = "White"
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
            return render_template("sign_in.html", session = session, view1 = view_dz1, view2 = view_dz2, view3 = view_dz3, view4 = view_dz4)
            session["sign_in"] = True
    session["sign_in"] = True
    return render_template("sign_in.html", session = session, view1 = view_dz1, view2 = view_dz2, view3 = view_dz3, view4 = view_dz4)

@app.route("/profile")
def profile():
    global view_dz1
    global view_dz2
    global view_dz3
    global view_dz4
    session["view_dz1"] = view_dz1
    session["view_dz2"] = view_dz2
    session["view_dz3"] = view_dz3
    session["view_dz4"] = view_dz4
    session["onpage"] = "profile"
    if  not "view_dz1" in session:
        session["view_dz1"] = view_dz1
    if not "view_dz2" in session:
        session["view_dz2"] = view_dz2
    if not "view_dz3" in session:
        session["view_dz3"] = view_dz3
    if not "view_dz4" in session:
        session["view_dz4"] = view_dz4
    if not "color" in session:
        session["txtcolor"] = "black"
        session["bgcolor"] = "white"
        session["color"] = "White"
    if not "user" in session:
        session["sign_in"] = False
        session["logged"] = False
        return redirect(url_for("sign_in"))
    session["act_home"] = ""
    session["act_feat"] = ""
    session["act_log"] = "active"
    session["sign"] = "Sign in"
    session["page_info"] = "You are on the profile page"
    return render_template("profile.html", values = users.query.filter_by(user=session["user"]).first(), session = session, view1 = view_dz1, view2 = view_dz2, view3 = view_dz3, view4 = view_dz4)

@app.route("/profile/<user>")
def user_profile(user):
    return render_template("user-profile.html", values = users.query.filter_by(user=user).first(), session = session, view1 = view_dz1, view2 = view_dz2, view3 = view_dz3, view4 = view_dz4)

@app.route("/profile/edit", methods= ["POST","GET"])
def edit_profile():
    global view_dz1
    global view_dz2
    global view_dz3
    global view_dz4
    session["view_dz1"] = view_dz1
    session["view_dz2"] = view_dz2
    session["view_dz3"] = view_dz3
    session["view_dz4"] = view_dz4
    session["onpage"] = "edit_profile"
    if  not "view_dz1" in session:
        session["view_dz1"] = view_dz1
    if not "view_dz2" in session:
        session["view_dz2"] = view_dz2
    if not "view_dz3" in session:
        session["view_dz3"] = view_dz3
    if not "view_dz4" in session:
        session["view_dz4"] = view_dz4
    if not "color" in session:
        session["txtcolor"] = "black"
        session["bgcolor"] = "white"
        session["color"] = "White"
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
    return render_template("edit_profile.html", values = users.query.filter_by(user=session["user"]).first(), session = session, view1 = view_dz1, view2 = view_dz2, view3 = view_dz3, view4 = view_dz4)

@app.route("/color/<page>")
def colorchanger(page):
    if session["color"] == "White":
        session["txtcolor"] = "LightGray"
        session["bgcolor"] = "#404040"
        session["color"] = "Black"
    elif session["color"] == "Black":
        session["txtcolor"] = "black"
        session["bgcolor"] = "white"
        session["color"] = "White"
    return redirect(url_for(page))

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
