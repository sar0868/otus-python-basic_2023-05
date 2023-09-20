from flask import request
from sqlalchemy import Sequence, delete, select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models import db, User, Post


def create_users(users_data: list):
    users = [
        User(
            name=el['name'],
            username=el['username'],
            email=el['email'],
        )
        for el in users_data
    ]
    db.session.add_all(users)
    db.session.commit()


def create_user(name: str, username: str, email: str = None) -> User:
    user = User(name=name, username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user


def get_users() -> list[User]:
    page = request.args.get('page', 1, type=int)
    users = User.query.order_by(User.id).paginate(per_page=5)
    return users


def get_user_by_id_or_raise(user_id: int) -> User:
    user: User = db.get_or_404(
        User,
        user_id,
        description=f"User #{user_id} not found!")
    return user


def delete_user(user: User) -> None:
    db.session.delete(user)
    db.session.commit()


def create_post(title: str, user_id: int, body: str = "") -> Post:
    post = Post(title=title, body=body, user_id=user_id)
    db.session.add(post)
    db.session.commit()
    return post


def create_posts(posts_data: list) -> None:
    posts = [
        Post(
            title=el['title'],
            body=el['body'],
            user_id=el['userId'],
        )
        for el in posts_data
    ]
    db.session.add_all(posts)
    db.session.commit()


def get_posts() -> list[Post]:
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.id).paginate(per_page=10)
    return posts


def get_post_by_id_or_raise(post_id: int) -> Post:
    post: Post = db.get_or_404(
        Post,
        post_id,
        description=f"Post #{post_id} not found!")
    return post


def get_posts_by_user_id_or_raise(user_id: int) -> list[Post]:
    # posts: list[Post] = db.get_or_404(

    # )
    pass


def delete_post(post: Post) -> None:
    db.session.delete(post)
    db.session.commit()
