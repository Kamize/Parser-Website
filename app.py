from fileinput import filename
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        return request.form["input"]


if __name__ == "__main__" :
    app.run(debug = True, host="127.0.0.1", port=5000)