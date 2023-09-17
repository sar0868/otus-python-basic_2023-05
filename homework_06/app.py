from flask import Flask, render_template, request


app = Flask(__name__)


@app.get("/", endpoint="index")
def get_index():
    return render_template("index.html")
