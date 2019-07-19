from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
def hello():
    name = "Harish kumawat bro"
    return render_template("index.html",name=name)

@app.route("/about")
def about():
    out = "Computer Science engineer"
    return render_template("about.html",work=out)

app.run(debug=True)