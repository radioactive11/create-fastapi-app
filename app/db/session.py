import contextlib
from typing import Any, Iterator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker

from app.config.config import POSTGRES_URI

# Get the sync version of the URI by removing the +asyncpg driver
SYNC_POSTGRES_URI = POSTGRES_URI.replace("+asyncpg", "")

Base = declarative_base()


class DatabaseSessionManager:
    def __init__(self, host: str, engine_kwargs: dict[str, Any] = {}):
        self._engine = create_engine(host, **engine_kwargs)
        self._sessionmaker = sessionmaker(
            autocommit=False, autoflush=False, bind=self._engine
        )

    def close(self):
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")
        self._engine.dispose()
        self._engine = None
        self._sessionmaker = None

    @contextlib.contextmanager
    def session(self) -> Iterator[Session]:
        if self._sessionmaker is None:
            raise Exception("DatabaseSessionManager is not initialized")

        session = self._sessionmaker()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


sessionmanager = DatabaseSessionManager(host=SYNC_POSTGRES_URI)


def get_db_session() -> Iterator[Session]:
    with sessionmanager.session() as session:
        yield session
