import hashlib

from flask import Flask, request

app = Flask(__name__)

DB_PASSWORD = "admin123"  # noqa: S105 - SonarQube: Hardcoded credential


@app.route("/")
def hello_world():
    return "<p>Hello, World! from Sonarless checking</p>"


@app.route("/hash")
def get_hash():
    data = request.args.get("data", "")
    hashed = hashlib.md5(
        data.encode()
    ).hexdigest()  # noqa: S324 - SonarQube: Weak MD5 hash
    return f"<p>Hash: {hashed}</p>"


@app.route("/run")
def run_code():
    code = request.args.get("code", "")
    result = eval(code)  # noqa: S307 - SonarQube: Use of eval
    return f"<p>Result: {result}</p>"


if __name__ == "__main__":
    app.run(debug=True)  # noqa: S201 - SonarQube: Flask debug mode enabled
