from cnxpool import cnxpool
from flask import Blueprint,request,render_template,redirect

Signup=Blueprint('Signup',__name__)

@Signup.route('/signup',methods=["POST"])
def signup():
    cnx=cnxpool.get_connection()
    cursor=cnx.cursor()
    nameData=request.form.get("membername")
    accountData=request.form.get("account1")
    passwordData=request.form.get("password1")
    cursor.execute("SELECT `username` from `member` WHERE `username`='"+accountData+"';")
    checkregisterData=cursor.fetchall()
    if nameData=="" or accountData=="" or passwordData=="":
        cursor.close()
        cnx.close()
        return redirect("/error/?message=請輸入註冊資料")
    elif not checkregisterData == []:
        cursor.close()
        cnx.close() 
        return redirect("/error/?message=帳號已經被註冊")  
    else:
        cursor.execute("INSERT INTO `member` (`name`,`username`,`password`) SELECT'"+nameData+"','"+accountData+"','"+passwordData+"'FROM DUAL WHERE NOT EXISTS (SELECT `username` FROM `member` WHERE `username`='"+accountData+"');")
        cursor.close()
        cnx.commit()
        cnx.close() 
        return render_template("week7_frontpage.html")