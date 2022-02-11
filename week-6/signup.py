import mysql.connector
from flask import Blueprint,request,render_template,redirect

Signup=Blueprint('Signup',__name__)

@Signup.route('/signup',methods=["POST"])
def signup():
    connection=mysql.connector.connect(host='localhost',
                                      port='3306',
                                      user='root',
                                      password='123456',
                                      database='website',
                                      buffered=True,)
    cursor=connection.cursor()
    nameData=request.form.get("membername")
    accountData=request.form.get("account1")
    passwordData=request.form.get("password1")
    cursor.execute('SELECT `username` FROM `member`;')
    accountName=cursor.fetchall()
    if nameData=="" or accountData=="" or passwordData=="":
        cursor.close()
        connection.commit()
        connection.close()
        return redirect("/error/?message=請輸入註冊資料")
    elif (accountData,) not in accountName:
        cursor.execute("INSERT INTO `member` (`name`,`username`,`password`) SELECT'"+nameData+"','"+accountData+"','"+passwordData+"'FROM DUAL WHERE NOT EXISTS (SELECT `username` FROM `member` WHERE `username`='"+accountData+"');")
        cursor.close()
        connection.commit()
        connection.close() 
        return render_template("week6_frontpage.html")
    else:
        cursor.close()
        connection.commit()
        connection.close() 
        return redirect("/error/?message=帳號已經被註冊")
    
    