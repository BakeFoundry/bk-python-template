from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!!!fetch AMI id, ok lets make some change</p>"


if __name__ == "__main__":
    app.run(debug=True)
