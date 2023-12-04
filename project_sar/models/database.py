import asyncio

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_scoped_session,
)
from sqlalchemy.orm import sessionmaker

import config

engine = create_async_engine(
    url=config.ASYNC_DB_URL,
    echo=config.DB_ECHO,
)

session_factory = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)

AsyncScopedSession = async_scoped_session(
    session_factory,
    scopefunc=asyncio.current_task,
)


async def scoped_session_dependency() -> AsyncSession:
    session = AsyncScopedSession()
    yield session
    await session.close()
