# app.py
from flask import Flask, render_template, request, jsonify
from rag_pipeline import ask_rag

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message")
    if not user_msg:
        return jsonify({"error": "Empty message"}), 400
    answer = ask_rag(user_msg)
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(debug=True)
