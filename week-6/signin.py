import mysql.connector
from flask import Blueprint, request,session,redirect,url_for

Signin=Blueprint('Signin',__name__)

@Signin.route("/signin",methods=["POST"])
def signin():
    connection=mysql.connector.connect(host='localhost',
                                      port='3306',
                                      user='root',
                                      password='123456',
                                      database='website',)
    cursor=connection.cursor()
    cursor.execute('SELECT `username` FROM `member`;')
    accountName=cursor.fetchall()
    cursor.execute('SELECT `password` FROM `member`;')
    passwordName=cursor.fetchall()
    cursor.close()
    connection.commit()
    connection.close() 
    if (request.form.get("account2"),) in accountName and (request.form.get("password2"),) in passwordName:
        user=request.form.get("account2")
        session["user"]=user
        return redirect(url_for("Member.member"))  
    elif request.form.get("account2")=="" or request.form.get("password2")=="":
        return redirect("/error/?message=請輸入帳號、密碼")
    else:
        return redirect("/error/?message=帳號、或密碼輸入錯誤")