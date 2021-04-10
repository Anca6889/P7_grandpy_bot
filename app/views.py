from flask import render_template, jsonify, request
from . import app

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ajax", methods=["POST"])
def ajax():
    user_text = request.form["userText"] #cherche dans le name de inp
    print(user_text)
    return jsonify(["pas de réponse"])