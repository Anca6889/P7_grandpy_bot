from flask import render_template, jsonify, request
from . import app
from app.parser import Parser
from app.requester import Request
from app.config import config as c
import random

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ajax", methods=["POST"])
def ajax():
    user_text = request.form["userText"]#cherche dans le name de input html
    parser = Parser(user_text) 
    result = Request(parser.cleaned)
    answer = result.wiki_result
    return jsonify(answer)
