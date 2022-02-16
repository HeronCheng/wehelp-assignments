from flask import Blueprint, session, redirect, render_template


Member=Blueprint('Member',__name__)

@Member.route("/member/")
def member():
    if "user" in session:
        name=session.get("name")
        return render_template("week7_member.html",memberName=name)
    else:
        return redirect("/")