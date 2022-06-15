from flask import Flask, jsonify, render_template, url_for, request

from lexical_analyzer import sentence_to_tokens
from pda_parser import swedish_grammar_parse

app = Flask(__name__)

# Main page of the app
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

# Route for API call
@app.route("/grammar")
def grammar():
    sentence = request.args.get("sentence")
    data = swedish_grammar_parse(sentence)
    return jsonify(data)

if __name__ == "__main__" :
    app.run(debug = False, host="0.0.0.0", port=5000)