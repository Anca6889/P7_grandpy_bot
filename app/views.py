from flask import render_template, jsonify, request
from . import app
from app.parser import Parser

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ajax", methods=["POST"])
def ajax():
    user_text = request.form["userText"]#cherche dans le name de input html
    answer = user_text.upper()
    print(user_text)
    parser = Parser()
    print(parser.split_message(user_text))
    return jsonify(answer)
