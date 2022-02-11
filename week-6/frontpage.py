from flask import Blueprint, render_template

Frontpage=Blueprint('Frontpage',__name__)

@Frontpage.route("/")
def frontpage():
    return render_template("week6_frontpage.html")