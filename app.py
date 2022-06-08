from dataclasses import dataclass
from fileinput import filename
from flask import Flask, jsonify, render_template, url_for, request

from lexical_analyzer import sentence_to_tokens

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/grammar")
def grammar():
    sentence = request.args.get("sentence")
    data = {"tokens":sentence_to_tokens(sentence)}
    return jsonify(data)

if __name__ == "__main__" :
    app.run(debug = False, host="192.168.1.7", port=9999)