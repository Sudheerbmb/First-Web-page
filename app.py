from flask import Flask,render_template
app= Flask(__name__)

@app.route("/")
def start():
    return "Starting"

@app.route("/mbsa")
def mbsa():
    return render_template("index.html")



