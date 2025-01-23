from Framai import PythonElectron
from flask import Flask, jsonify

app = PythonElectron()

@app.app.route("/api/message", methods=["GET"])
def get_message():
    return jsonify({"message": "Olá do backend em Python!"})

if __name__ == "__main__":
    app.start_backend()
    app.start_frontend("index.html")
