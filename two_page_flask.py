from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Harishkumawat2610"

@app.route("/about")
def about():
    return "I am a Computer Science Engineer"

app.run()
