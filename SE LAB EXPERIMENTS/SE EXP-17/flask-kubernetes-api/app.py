from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Flask API is running successfully",
        "project": "Docker and Kubernetes"
    })

@app.route("/hello")
def hello():
    return jsonify({
        "message": "Hello from the Flask API!"
    })

@app.route("/status")
def status():
    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)