from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ License Server is Running!"

@app.route("/validate", methods=["GET"])
def validate():
    machine_id = request.args.get("id")
    try:
        with open("whitelist.json") as f:
            data = json.load(f)
        if machine_id in data.get("allowed", []):
            return jsonify({"status": "authorized"})
        else:
            return jsonify({"status": "denied"}), 403
    except Exception as e:
        return jsonify({"status": "error", "details": str(e)}), 500
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render sets PORT env var
    app.run(host="0.0.0.0", port=port)
