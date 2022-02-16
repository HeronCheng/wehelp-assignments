from flask import Flask

from frontpage import Frontpage
from error import Error
from signin import Signin
from member import Member
from signout import Signout
from signup import Signup
from query import Query
from modify import Modify

app=Flask(__name__)
app.secret_key="abcdefghijklmnopqrstuvwxyz"

app.register_blueprint(Frontpage)
app.register_blueprint(Error)
app.register_blueprint(Signin)
app.register_blueprint(Member)
app.register_blueprint(Signout)
app.register_blueprint(Signup)
app.register_blueprint(Query)
app.register_blueprint(Modify)



app.run(port=3000)