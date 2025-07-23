from flask import Flask, request, jsonify

app = Flask(__name__)

notverygoodnames = ["bad", "offensive", "dummy", "add more"]

@app.route("/cfbn", methods=["POST"])
def CheckForBadName():
    data = request.get_json()
    fa = data.get("FunctionArgument", {})
    name = fa.get("name", "").lower()

    if any(bad in name for bad in notverygoodnames):
        return jsonify({"result": 2}), 200
    return jsonify({"result": 0}), 200
