from flask import Flask

app = Flask(__name__)  # I think this is right? Should be for single module

@app.route("/")
def index():
    # todo: make the homepage and put it into a html file
    return "<p>Hello, World!</p>" 


