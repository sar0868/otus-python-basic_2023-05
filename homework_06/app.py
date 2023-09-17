from os import getenv
from flask import Flask, render_template, request
from flask_migrate import Migrate
from models import db


app = Flask(__name__)
config_name = getenv("CONFIG_NAME", "DevelopmentConfig")
app.config.from_object(f"config.{config_name}")

db.init_app(app=app)
migrate = Migrate(app=app, db=db)


@app.get("/", endpoint="index")
def get_index():
    return render_template("index.html")
