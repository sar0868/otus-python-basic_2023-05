import crud
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import User

from .forms.user import UserForm

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


@users_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def create_user():
    form = UserForm()
    if request.method == "GET":
        return render_template("users/add.html", form=form)
    if not form.validate_on_submit():
        return render_template("users/add.html", form=form), 400
    user = crud.create_user(
        name=form.data["name"],
        username=form.data["username"],
        email=form.data["email"],
    )
    url = url_for("users_app.detail",
                  user_id=user.id)
    flash(f'Create user {user.name!r}', category="primary")
    return redirect(url)


@users_app.route("/<int:user_id>/confirm-delete/",
                 methods=["GET", "POST"],
                 endpoint="confirm-delete",
                 )
def confirm_delete_user(user_id: int):
    user = crud.get_user_by_id_or_raise(user_id)
    if request.method == "GET":
        return render_template("users/confirm-delete.html", user=user)
    user_name = user.name
    crud.delete_user(user)
    flash(f'Deleted user {user_name!r}', category="warning")
    return redirect(url_for("users_app.users"))
