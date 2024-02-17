from flask import Flask

# flask --app main run

app = Flask(__name__)

@app.route("/")
def hello_world():
    res = {
        "message": "why hello there!",
        "other_stuff": "you should give us da dub!"
    }
    return res