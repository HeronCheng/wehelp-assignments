from flask import Blueprint, request,session,redirect,url_for
from cnxpool import cnxpool

Signin=Blueprint('Signin',__name__)

@Signin.route("/signin",methods=["POST"])
def signin():
    cnx=cnxpool.get_connection()                                   
    cursor=cnx.cursor()
    account=request.form.get("account2")
    password=request.form.get("password2")
    cursor.execute("SELECT `name`,`username`,`password` from `member` WHERE `username`='"+account+"' and `password`='"+password+"';")
    checkData=cursor.fetchall()
    cursor.close()
    cnx.close()
    if account=="" or password=="":
        return redirect("/error/?message=請輸入帳號、密碼")  
    elif checkData == []:
        return redirect("/error/?message=帳號或密碼輸入錯誤")
    else:
        name=checkData[0][0]
        user=account
        session["user"]=user
        session["name"]=name
        return redirect(url_for("Member.member"))