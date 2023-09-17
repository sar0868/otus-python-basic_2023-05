from typing import Sequence

from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest

from models import db, User

products_app = Blueprint(
    "users_app",
    __name__,
    url_prefix="/users",
)


@products_app.get("/", endpoint="list")
def get_products_list():
    pass
    # stmt = select(User).order_by(User.id)
    # # products = db.session.execute(stmt).scalars()
    # products: Sequence[User] = db.session.scalars(stmt)
    # return render_template(
    #     "products/index.html",
    #     products=products,
    # )
