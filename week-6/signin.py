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
    account=request.form.get("account2")
    password=request.form.get("password2")
    cursor.execute("SELECT `username`,`password` from `member` WHERE `username`='"+account+"' and `password`='"+password+"';")
    checkData=cursor.fetchall()
    cursor.execute("SELECT `name` FROM `member` WHERE `username`='"+account+"';")
    name=cursor.fetchone()[0]
    cursor.close()
    connection.close()     
    if account=="" or password=="":
        return redirect("/error/?message=請輸入帳號、密碼")  
    elif checkData == []:
        return redirect("/error/?message=帳號或密碼輸入錯誤")
    else:
        user=account
        session["user"]=user
        session["name"]=name
        return redirect(url_for("Member.member"))