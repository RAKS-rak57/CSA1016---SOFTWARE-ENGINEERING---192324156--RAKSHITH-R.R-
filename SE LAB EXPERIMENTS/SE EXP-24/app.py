
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "EXP-24 CI/CD Pipeline is running successfully!",
        "application": "Containerized Flask Application",
        "deployment": "GitHub Actions + Docker Hub + Azure"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

