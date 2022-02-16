from cnxpool import cnxpool
from flask import request,jsonify,Blueprint

Query=Blueprint("Query",__name__)

@Query.route("/api/members",methods=["GET"])
def query():
    data=request.args.get("username",None)
    cnx=cnxpool.get_connection()
    cursor=cnx.cursor()
    cursor.execute("SELECT `id`,`name`,`username` FROM `member` WHERE `username`='"+data+"';")
    result=cursor.fetchall()
    cursor.close()
    cnx.close()
    if result == []:
        return jsonify({"data":None})
    else:
        id=result[0][0]
        name=result[0][1]
        username=result[0][2]
        return jsonify({"data":{"id":id,"name":name,"username":username}})
