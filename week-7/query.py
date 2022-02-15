import mysql.connector
from flask import request,jsonify,Blueprint

Query=Blueprint("Query",__name__)

@Query.route("/api/members",methods=["GET"])
def query():
    data=request.args.get("username",None)
    connection=mysql.connector.connect(host='localhost',
                                       port='3306',
                                       user='root',
                                       password='123456',
                                       database='website',
                                       buffered=True,)
    cursor=connection.cursor()
    cursor.execute("SELECT `id`,`name`,`username` FROM `member` WHERE `username`='"+data+"';")
    result=cursor.fetchall()
    cursor.close()
    connection.close()
    if result == []:
        return jsonify({"data":None})
    else:
        id=result[0][0]
        name=result[0][1]
        username=result[0][2]
        return jsonify({"data":{"id":id,"name":name,"username":username}})
