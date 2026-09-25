from flask import Flask

app = Flask(__name__)

existing_models = ["Beedle", "Crossroads"]


@app.route("/")
def index():
    return "Welcome to Flatiron Cars"


@app.route("/<model>")
def model(model):
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"