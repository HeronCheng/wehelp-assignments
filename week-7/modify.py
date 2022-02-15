import mysql.connector
from flask import Blueprint, session,request,jsonify

Modify=Blueprint("Modify",__name__)

@Modify.route("/api/member",methods=["POST"])
def modify():
    connection=mysql.connector.connect(host='localhost',
                                       port='3306',
                                       user='root',
                                       password='123456',
                                       database='website',
                                       buffered=True,)
    cursor=connection.cursor()
    originName=session.get("name")
    newName=request.get_json()["name"]
    cursor.execute("UPDATE `member` SET `name`='"+newName+"' WHERE `name`='"+originName+"';")
    cursor.close()
    connection.commit()
    connection.close()
    if "user" not in session:
        return jsonify({"error":True})
    else:
        session["name"]=newName
        return jsonify({"ok":True})