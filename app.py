from flask import Flask, render_template, request, redirect,session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine("postgres://qptheqjsntkxdz:d9bc924f7dfc78d025e3aa73e40fb72b5ef686c45cb48ef0995a0de7a5d10e98@ec2-54-83-192-245.compute-1.amazonaws.com:5432/ddm187fm4o561e")
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
