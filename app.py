import os
import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "GhostTrack Service is Active!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
