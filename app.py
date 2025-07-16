# app.py

from flask import Flask, request, jsonify, render_template
from clipboard_data import set_clipboard, get_clipboard

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")  # Optional UI

@app.route('/clipboard', methods=['GET'])
def get_clipboard_route():
    return jsonify({"clipboard": get_clipboard()})

@app.route('/clipboard', methods=['POST'])
def set_clipboard_route():
    data = request.get_json()
    text = data.get("text", "")
    set_clipboard(text)
    return jsonify({"message": "Clipboard updated", "clipboard": text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)

