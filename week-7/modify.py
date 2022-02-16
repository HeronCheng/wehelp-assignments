from cnxpool import cnxpool
from flask import Blueprint, session,request,jsonify

Modify=Blueprint("Modify",__name__)

@Modify.route("/api/member",methods=["POST"])
def modify():
    cnx=cnxpool.get_connection()
    cursor=cnx.cursor()
    originName=session.get("user")
    newName=request.get_json()["name"]
    cursor.execute("UPDATE `member` SET `name`='"+newName+"' WHERE `username`='"+originName+"';")
    cursor.close()
    cnx.commit()
    cnx.close()
    if "user" not in session:
        return jsonify({"error":True})
    else:
        session["name"]=newName
        return jsonify({"ok":True})