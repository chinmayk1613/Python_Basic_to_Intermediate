from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1613@localhost/Info'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id_db=db.Column(db.Integer,primary_key=True)
    name_db=db.Column(db.String(120))
    email_db=db.Column(db.String(120),unique=True)
    height_db=db.Column(db.Integer)

    def __init__(self, name_db, email_db, height_db):
        self.name_db=name_db
        self.email_db=email_db
        self.height_db=height_db


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        uname=request.form["user_name"]
        uemail=request.form["user_email"]
        uheight=request.form["user_height"]
        print(uname,uemail,uheight)
        if db.session.query(Data).filter(Data.email_db==uemail).count()==0:
            data=Data(uname, uemail, uheight)
            db.session.add(data)
            db.session.commit()
            return render_template("success.html")
    return render_template('index.html',
    text="This email ID is already present,please enter unique email id!!")
if __name__=='__main__':
   app.debug=True
   app.run()
