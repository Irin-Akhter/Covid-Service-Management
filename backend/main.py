from flask import Flask,redirect,render_template
from flask_sqlalchemy import SQLAlchemy

# mydatabase connection
local_server=True
app=Flask(__name__)
app.secret_key="aneesrehmankhan"

# app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:password@localhost/databsename'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/covid'
db=SQLAlchemy(app)

class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))

@app.route("/")
def home():
   
    return render_template("index.html")

# testing wheather db is connected or not  
@app.route("/test")
def test():
    try:
        a=Test.query.all()
        print(a)
        return f'MY DATABASE IS CONNECTED '
    except Exception as e:
        print(e)
        return f'MY DATABASE IS NOT CONNECTED {e}'


app.run(debug=True)