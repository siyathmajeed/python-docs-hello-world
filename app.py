from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Mr mohamed siyath welcome to programming!"
    
