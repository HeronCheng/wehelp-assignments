from flask import session, Blueprint, redirect

Signout=Blueprint('Signout',__name__)

@Signout.route("/signout")
def signout():
    session.pop("user",None)
    return redirect("/")