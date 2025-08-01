# app.py

from flask import Flask, request, jsonify, render_template
from clipboard_data import set_clipboard, get_clipboard
import random
from itertools import cycle

app = Flask(__name__)

gif_urls = [
    "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2pjcTJ2anhrZ3lodGUxc213aDRtODdmZnV6OHFuNjQxOWpjN3R5dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/12qHWnTUBzLWXS/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3cW1kc3JudGtqb3V3b3hkdjM5cXFhM2N2ZTJzNnFwdzdwaXJvZnM1dCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/nWF3AYzIGCrg4/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3cW1kc3JudGtqb3V3b3hkdjM5cXFhM2N2ZTJzNnFwdzdwaXJvZnM1dCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/RGLkqjTQ7ehZS/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3cW1kc3JudGtqb3V3b3hkdjM5cXFhM2N2ZTJzNnFwdzdwaXJvZnM1dCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/Dh7hDuJoSVXdm/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3anYzNDB0bWwxZnhsZXR0NWp4eGk4dzF4Z3l2c3dmYzM3b2d1OThpOCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/3o72FaTrfa7aMX0UqA/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3anYzNDB0bWwxZnhsZXR0NWp4eGk4dzF4Z3l2c3dmYzM3b2d1OThpOCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/DmwX5R07PmaUE/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3aTV4NG5nY281bGJtNDZzeTJoMnJ3cnJuY2hxdHN0d2JwcmFxajNkdyZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/dVoCGo2PlJLIYQR0UR/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3MWF3djJxZGdjcTkwa3BxeDB2dnpnZWwyenI0ZzFrbGNwampkN3FwOSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/8L17z7N2tOCxMDlfE0/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3Z255b3VlcWFjamxuenNsaXFxY2NrZHFkNHo4ZTJoMTlybTZwanF4YiZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/gK99k8iMtKeJ2/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3Z255b3VlcWFjamxuenNsaXFxY2NrZHFkNHo4ZTJoMTlybTZwanF4YiZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/VehoU0h2Rl8Gc/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3Z255b3VlcWFjamxuenNsaXFxY2NrZHFkNHo4ZTJoMTlybTZwanF4YiZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/QJVxNH8uJk9c4/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3Z255b3VlcWFjamxuenNsaXFxY2NrZHFkNHo4ZTJoMTlybTZwanF4YiZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/pZQE3FFvBBhvO/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3YWl6dDJ4MmM5NnduYTM3cmUzeGp1YTVkMHdnNHZiandzYWp2Z2dqbyZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/qzKGfKDGPZCj6/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3Y2tiZzN1YnowanRjYjZpZXpxN21uNGU3ZDNqZzI2enRoeG1kczdrdCZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/2R1QSI7WEUF4A/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3NDMxemFvZ3JodW5ubW4wYWg1c3Nuc2EzdHBndzV6cmI0Mjg3YjlyNyZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/uSlkwemszvnTq/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3NDMxemFvZ3JodW5ubW4wYWg1c3Nuc2EzdHBndzV6cmI0Mjg3YjlyNyZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/HPjDl4Ta9SUjC/giphy.gif",

    "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3a2s0dzN2ZXkyZDhqMnJ4ZnJudXNnZGd4azQ0djVrZGFvbnpiY2JobyZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/107DVlddpQEWXK/giphy.gif"
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

gif_cycle = cycle(gif_urls)

@app.route('/getGifUrl', methods=['GET'])
def get_gif_url():
    url = next(gif_cycle)
    return jsonify({"gif_url": url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True)
