# app.py

from flask import Flask, request, jsonify, render_template
from clipboard_data import set_clipboard, get_clipboard

app = Flask(__name__)

gif_urls = [
    "https://raw.githubusercontent.com/plateau11/test99/main/1f5832186ffd64058efad2a3a810d006.gif",
    "https://raw.githubusercontent.com/plateau11/test99/main/0e1f8367d81e6f161d198a0b5011a62f.gif",
    "https://raw.githubusercontent.com/plateau11/test99/main/92cdfc9bdebc53a747331999b6933734.gif",
    "https://raw.githubusercontent.com/plateau11/test99/main/tumblr_nnozvnkRtE1uuzayro1_1280.gif"
]

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

@app.route('/getGifUrl', methods=['GET'])
def get_gif_url():
    selected_url = random.choice(gif_urls)
    return jsonify({"gif_url": selected_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
