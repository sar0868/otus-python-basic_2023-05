"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio

from sqlalchemy import Result, literal, select
from sqlalchemy.ext.asyncio import AsyncSession

from models import (
    User,
    Post,
    engine,
    Session,
)
import crud
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data


async def run_queries():
    async with Session() as session:
        ...

        # async with session_dependency() as session:
        # await crud.create_user(session=session, username="Alex", name="Alex JJJ")
        # await crud.create_user(session=session, username="John", name="John Smit", email="john_sm@example.com")
        # await crud.delete_user()
        # users_data: list[User]
        # posts_data: list[Post]
        # users_data, posts_data = await asyncio.gather(
        #     fetch_users_data(),
        #     fetch_posts_data(),
        # )
        # await crud.clear_table_users(session=session)
        # await crud.clear_table_posts(session=session)
        # await crud.create_users(session=session, users_data=users_data)
        # await crud.create_posts(session=session, posts_data=posts_data)
        # # await crud.create_post(session=session, post_in=Post(title="hello", user_id=1))
        # await crud.get_users(session=session)


async def fetch_user():
    result = await fetch_users_data()
    print(type(result))
    print(result)


async def fetch_posts():
    result = await fetch_posts_data()
    print(result)


async def async_main():
    await run_queries()
    # await fetch_user()
    # await fetch_posts()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    asyncio.run(async_main())
