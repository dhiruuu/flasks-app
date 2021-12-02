from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
x=int(3)
y=int(5)
 if x > y:
         print ("y is greater than x") 
