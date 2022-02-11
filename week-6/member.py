from flask import Blueprint, session, redirect, render_template,request
import mysql.connector


Member=Blueprint('Member',__name__)

@Member.route("/member/")
def member():
    if "user" in session:
        connection=mysql.connector.connect(host='localhost',
                                           port='3306',
                                           user='root',
                                           password='123456',
                                           database='website',)
        cursor=connection.cursor()
        account=session.get("user")
        cursor.execute("SELECT `name` FROM `member` WHERE `username`='"+account+"';")
        user=cursor.fetchone()[0]
        realUser=str(user)
        cursor.close()
        connection.close()
        return render_template("week6_member.html",memberName=realUser)
    else:
        return redirect("/")