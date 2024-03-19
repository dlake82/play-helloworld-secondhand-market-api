from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.core.config import settings
from app.crud.crud import CRUD

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]


def get_crud(sessions: SessionDep) -> Generator[CRUD, None, None]:
    yield CRUD(db=sessions)


CrudDep = Annotated[CRUD, Depends(get_crud)]
