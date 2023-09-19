from sqlalchemy import delete, select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models import db, User, Post


def create_users(users_data: list):
    users = [
        User(
            id=el['id'],
            name=el['name'],
            username=el['username'],
            email=el['email'],
        )
        for el in users_data
    ]
    db.session.add_all(users)
    db.session.commit()


def create_user(name: str, username: str, email: str = None) -> None:
    user = User(name=name, username=username, email=email)
    db.session.add(user)
    db.session.commit()


# def get_users() -> list[User]:
#     stmt = (
#         select(User)
#         .order_by(User.id)
#     )
#     result: Result = db.session.execute(stmt)
#     users: list[User] = result.scalars().all()
#     print(users)
#     return users


def create_post(title: str, user_id: int, body: str = "") -> None:
    post = Post(title=title, body=body, user_id=user_id)
    db.session.add(post)
    db.session.commit()


def create_posts(posts_data: list) -> None:
    posts = [
        Post(
            id=el['id'],
            title=el['title'],
            body=el['body'],
            user_id=el['userId'],
        )
        for el in posts_data
    ]
    db.session.add_all(posts)
    db.session.commit()


def delete_user(user_id: int) -> None:
    stmt = (
        delete(User)
        .where(User.id == user_id)

    )
    db.session.execute(stmt)
    db.session.commit()


def clear_table_users() -> None:
    stmt = (
        delete(User)
    )
    db.session.execute(stmt)
    db.session.commit()


def delete_post(post_id: int) -> None:
    stmt = (
        delete(Post)
        .where(Post.id == post_id)

    )
    db.session.execute(stmt)
    db.session.commit()


def clear_table_posts() -> None:
    stmt = (
        delete(Post)
    )
    db.session.execute(stmt)
    db.session.commit()
