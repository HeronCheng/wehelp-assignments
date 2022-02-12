from flask import Blueprint, session, redirect, render_template,request
import mysql.connector


Member=Blueprint('Member',__name__)

@Member.route("/member/")
def member():
    if "user" in session:
        name=session.get("name")
        return render_template("week6_member.html",memberName=name)
    else:
        return redirect("/")