from flask import Flask,render_template,request,redirect
from mongoengine import Document , StringField , IntField,EmailField
import mlab



app = Flask(__name__)

@app.route('/register', methods = ['GET','POST'] )
def register():
    if request.method == "GET":
      return render_template("register.html")
    else:
      mlab.connect()

      class User(Document):
        name = StringField()
        email = EmailField()
        username = StringField()
        password = StringField()

      user = User (
        name = request.form["name"],
        email = request.form["email"],
        username = request.form["username"],
        password = request.form["password"]
      )
      user.save()
    return "wellcome"


if __name__ == '__main__':
  app.run(debug=True)