from flask import Flask,request,render_template,redirect,session,url_for

from frontpage import Frontpage
from error import Error
from signin import Signin
from member import Member
from signout import Signout
from signup import Signup

app=Flask(__name__)
app.secret_key="abcdefghijklmnopqrstuvwxyz"

app.register_blueprint(Frontpage)
app.register_blueprint(Error)
app.register_blueprint(Signin)
app.register_blueprint(Member)
app.register_blueprint(Signout)
app.register_blueprint(Signup)

app.run(port=3000)