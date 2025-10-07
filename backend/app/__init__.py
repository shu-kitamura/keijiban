import os
from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine


def get_session():
    with Session(engine) as session:
        yield session

database_url = os.getenv("DATABASE_URL")
engine = create_engine(database_url, echo=True, future=True)
sessionDep = Annotated[Session, Depends(get_session)]
