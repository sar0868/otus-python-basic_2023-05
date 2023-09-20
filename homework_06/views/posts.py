from typing import Sequence

from flask import Blueprint, render_template, request, redirect, url_for, flash
import crud
from .forms.post import PostForm

from models import Post

posts_app = Blueprint(
    "posts_app",
    __name__,
    url_prefix="/posts",
)


@posts_app.get("/", endpoint="posts")
def get_posts_list():
    # page = request.args.get('page', 1, type=int)
    # pagination = Post.query.order_by(Post.id).paginate(per_page=10)

    # return render_template("posts/index.html", pagination=pagination)
    return render_template("posts/index.html", posts=crud.get_posts())
    # return render_template("posts/index.html", posts=crud.get_posts())


@posts_app.get("/<int:post_id>/", endpoint="detail")
def get_post_by_id(post_id: int) -> Post:
    post = crud.get_post_by_id_or_raise(post_id)
    return render_template(
        "posts/detail.html",
        post=post,
        user_name=crud.get_user_by_id_or_raise(post.id).name
    )


@posts_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def create_post():
    form = PostForm()
    if request.method == "GET":
        return render_template("posts/add.html", form=form)
    if not form.validate_on_submit():
        return render_template("posts/add.html", form=form), 400
    post = crud.create_post(
        title=form.data["title"],
        body=form.data["body"],
        user_id=form.data["user_id"],
    )
    url = url_for("posts_app.detail",
                  post_id=post.id)
    flash(f'Create post {post.title!r}', category="primary")
    return redirect(url)


@posts_app.route("/<int:post_id>/confirm-delete/",
                 methods=["GET", "POST"],
                 endpoint="confirm-delete",
                 )
def confirm_delete_post(post_id: int):
    post = crud.get_post_by_id_or_raise(post_id)
    if request.method == "GET":
        return render_template("posts/confirm-delete.html", post=post)
    post_title = post.title
    crud.delete_post(post)
    flash(f'Deleted post {post_title!r}', category="warning")
    return redirect(url_for("posts_app.posts"))
