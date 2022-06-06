from dataclasses import dataclass
from fileinput import filename
from flask import Flask, jsonify, render_template, url_for, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/grammar")
def grammar():
    data = {"sentence" : request.args.get("sentence")}
    return jsonify(data)

if __name__ == "__main__" :
    app.run(debug = True, host="127.0.0.1", port=5000)