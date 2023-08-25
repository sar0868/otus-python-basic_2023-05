# """
# создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
# """

import asyncio
from aiohttp import ClientSession

USERS_DATA_URL = "http://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "http://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str) -> dict:

    async with ClientSession() as session:
        async with session.get(url) as response:
            data: dict = await response.json()
            return data


async def fetch_users_data():
    return await fetch_json(USERS_DATA_URL)


async def fetch_posts_data():
    return await fetch_json(POSTS_DATA_URL)


# async def main():
#     # result = await get_data(USERS_DATA_URL)
#     result = await fetch_posts_data()
#     for post in result:
#         print(f'user_id:{post["userId"]}, title= {post["title"]}')
#
#
# if __name__ == '__main__':
#     asyncio.run(main())