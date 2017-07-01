from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello, world!"

@app.route("/hey")
def helloes():
  return "Hey, world!"


if __name__ == "__main__":
  app.run()
