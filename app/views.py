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
def send_answer():
    user_text = request.form["userText"]#cherche dans le name de input html
    parser = Parser(user_text) 
    result = Request(parser.cleaned)
    print(result.lat, result.lng)
    answer = result.wiki_result
    lat = result.lat
    lng = result.lng
    return jsonify({"answer": answer, "lat": lat, "lng": lng})

