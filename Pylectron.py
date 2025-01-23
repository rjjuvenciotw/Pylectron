import webview
from flask import Flask, jsonify
from threading import Thread

class Pylectron:
    def __init__(self, host="127.0.0.1", port=5000):
        self.host = host
        self.port = port
        self.app = Flask(__name__)

    def add_route(self, route, handler, methods=["GET"]):
        self.app.route(route, methods=methods)(handler)

    def start_backend(self):
        def run():
            self.app.run(host=self.host, port=self.port, debug=False)
        self.backend_thread = Thread(target=run, daemon=True)
        self.backend_thread.start()

    def start_frontend(self, html_file):
        with open(html_file, "r", encoding="utf-8") as f:
            html = f.read()
        webview.create_window("Python Electron", html=html)
        webview.start()
