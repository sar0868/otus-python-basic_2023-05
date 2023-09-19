from typing import Sequence

from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest
import crud

from models import db, User

users_app = Blueprint(
    "users_app",
    __name__,
    url_prefix="/users",
)


@users_app.get("/", endpoint="users")
def get_users_list():
    return render_template("users/index.html", users=crud.get_users())


@users_app.get("/<int:user_id>/", endpoint="detail")
def get_user_by_id(user_id: int) -> User:
    return render_template(
        "users/detail.html",
        user=crud.get_user_by_id_or_raise(user_id),
    )
