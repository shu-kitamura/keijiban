from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, create_engine


def get_session():
    with Session(engine) as session:
        yield session

pg_url = "postgresql://user:password@db:5432/dev"
engine = create_engine(pg_url, echo=True, future=True)
sessionDep = Annotated[Session, Depends(get_session)]
