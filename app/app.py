from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    user_agent = request.headers.get('User-Agent')
    if user_agent == 'h4ck3r':
        return "Hackers are not allowed!", 403

    return f"Hello, World -- {datetime.now()}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)