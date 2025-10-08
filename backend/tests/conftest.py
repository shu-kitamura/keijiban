import os
import sys
import tempfile
from collections.abc import Iterator
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel

TMP_DB_PATH = Path(tempfile.gettempdir()) / "keijiban_backend_test.db"
os.environ.setdefault("DATABASE_URL", f"sqlite+pysqlite:///{TMP_DB_PATH}")

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app import engine  # noqa: E402
from app.main import app  # noqa: E402


@pytest.fixture(autouse=True)
def prepare_database() -> Iterator[None]:
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    try:
        yield
    finally:
        SQLModel.metadata.drop_all(engine)
        engine.dispose()
        if TMP_DB_PATH.exists():
            TMP_DB_PATH.unlink()


@pytest.fixture()
def client() -> Iterator[TestClient]:
    with TestClient(app) as test_client:
        yield test_client
