from flask import render_template, jsonify, request
from . import app
from app.parser import Parser

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ajax", methods=["POST"])
def ajax():
    user_text = request.form["userText"]#cherche dans le name de input html
    parser = Parser(user_text)
    parser.regex()
    answer = 'Tu as bien dit: " ' + user_text.upper() + ' " Billy ?'
    return jsonify(answer)
