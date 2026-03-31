from flask import Flask, jsonify
import os
import random
import time

app = Flask(__name__)

INSTANCE_ID = os.getenv("INSTANCE_ID", "unknown")

@app.route("/api/info")
def info():
    delay = random.uniform(0.1, 0.5)
    time.sleep(delay)

    return jsonify({
        "instance_id": INSTANCE_ID,
        "delay": delay
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok", "instance": INSTANCE_ID})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)