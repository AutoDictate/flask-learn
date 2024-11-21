from flask import Flask
from html import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "Hello Makka!"

@app.route("/<name>")
def hello(name):
  return f"Hello, {escape(name)}!"


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
