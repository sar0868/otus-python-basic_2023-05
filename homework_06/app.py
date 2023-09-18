import asyncio
from os import getenv
from flask import Flask, render_template, request
from flask_migrate import Migrate
from models import db, Post, User
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data
import crud

app = Flask(__name__)
config_name = getenv("CONFIG_NAME", "DevelopmentConfig")
app.config.from_object(f"config.{config_name}")

db.init_app(app=app)
migrate = Migrate(app=app, db=db)
with app.app_context():
    db.drop_all()
    db.create_all()


def set_dates():
    with db.session as session:
        users_data: list[User]
        posts_data: list[Post]
        users_data, posts_data = asyncio.gather(
            fetch_users_data(),
            fetch_posts_data(),
        )
        crud.create_users(session=session, users_data=users_data)
        crud.create_posts(session=session, posts_data=posts_data)


@app.get("/", endpoint="index")
def get_index():
    return render_template("index.html")


set_dates()
