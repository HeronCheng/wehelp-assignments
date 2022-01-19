from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session, url_for

app=Flask(__name__)
app.secret_key="abcdefghijklmnopqrstuvwxyz"

@app.route("/")
def frontpage():
    return render_template("week4_frontpage.html")

@app.route("/error/")
def query():
    data=request.args.get("message",None)
    return render_template("week4_failure.html",string=data)

@app.route("/signin",methods=["POST"])
def signin():
    if request.form.get("account")=="test" and request.form.get("password")=="test":
        user=request.form.get("account")
        session["user"]=user
        return redirect(url_for("user"))
    elif request.form.get("account")=="" or request.form.get("password")=="":
        return redirect("/error/?message=請輸入帳號、密碼")
    else:
        return redirect("/error/?message=帳號、或密碼輸入錯誤")

@app.route("/member/")
def user():
    if "user" in session:
        return render_template("week4_member.html")
    else:
        return redirect("/")

@app.route("/signout")
def signout():
    session.pop("user",None)
    return redirect("/")

app.run(port=3000)