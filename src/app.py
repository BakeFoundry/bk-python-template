import os

from flask import Flask, request

app = Flask(__name__)

# Intentional Hardcoded Secret for Testing (Secret Scan)
DUMMY_API_KEY = "AKIA1234567890EXAMPLE"


@app.route("/")
def hello_world():
    return "<p>Hello, World!ok, test again with fixed sast code </p>"


@app.route("/ping")
def ping():
    hostname = request.args.get("hostname")
    # VULNERABLE: Direct command injection for SAST scan testing
    # An attacker can providing 'example.com; ls' to execute local commands
    if hostname:
        response = os.popen(f"ping {hostname}").read()
        return f"<pre>{response}</pre>"
    return "Please provide a hostname via ?hostname=", 400


if __name__ == "__main__":
    app.run(debug=True)
