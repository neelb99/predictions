from flask import Flask, render_template, request, redirect,session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine("postgresql://postgres:1677@localhost:5432/postgres")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "GET":
        matches = db.execute("SELECT * FROM matches order by id asc").fetchall()
        return render_template('index.html', matches = matches)
    else:
        matchname = request.form.get("name")
        matchwinner = request.form.get("winner")
        matchvir = request.form.get("vir")
        matchjeh = request.form.get("jeh")
        matchneel = request.form.get("neel")
        matchkani = request.form.get("kani")
        db.execute("INSERT INTO matches(name,winner,vir,jeh,neel,kani) VALUES(:name,:winner,:vir,:jeh,:neel,:kani)",{"name":matchname,"winner":matchwinner,"vir":matchvir,"jeh":matchjeh,"neel":matchneel,"kani":matchkani})
        db.commit()
        matches = db.execute("SELECT * FROM matches order by id asc").fetchall()
        return render_template('index.html', matches=matches)

@app.route("/add")
def add():
    return render_template('add.html')
