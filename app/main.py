from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/info")
def info():
    return jsonify({
        "app": "local-k8s-stack",
        "version": os.getenv("APP_VERSION", "0.1.0"),
        "environment": os.getenv("APP_ENV", "development")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)