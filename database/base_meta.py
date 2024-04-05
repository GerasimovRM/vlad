from pydantic import BaseModel
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from config import DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME, DATABASE_PORT, SQL_ECHO

Base = declarative_base()
print(f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}")
engine = create_engine(
    f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}",
    echo=SQL_ECHO)
session_factory = sessionmaker(engine, autocommit=False)

metadata = Base.metadata


class BaseSQLAlchemyModel(Base):
    __abstract__ = True

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def update_by_pydantic(self, model: BaseModel):
        self.update(**model.dict(exclude_none=True))


def get_session() -> Session:
    return session_factory()
