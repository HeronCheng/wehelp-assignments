from flask import Blueprint, render_template, request

Error=Blueprint('Error',__name__)

@Error.route("/error/")
def query():
    data=request.args.get("message",None)
    return render_template("week6_failure.html",string=data)