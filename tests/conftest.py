from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from fastapi.testclient import TestClient

import pytest

from models import PriorityEnum
from database import Base
from models import Task
from app import app, get_db

TEST_DB_URL = "sqlite:///:memory:"

test_engine = create_engine(
    url=TEST_DB_URL,
    echo=True,
    poolclass=StaticPool,
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(bind=test_engine, autocommit=False, autoflush=False)

@pytest.fixture(scope="session")
def setup_test_db():
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)

@pytest.fixture
def db_session(setup_test_db):
    session = TestingSessionLocal()
    yield session
    session.query(Task).delete()
    session.commit()
    session.close()

@pytest.fixture
def client(db_session):
    def _override_get_db():
        yield db_session
    app.dependency_overrides[get_db] = _override_get_db
    test_client = TestClient(app)
    yield test_client
    app.dependency_overrides.clear()

@pytest.fixture
def sample_task(db_session):
    task = Task(
        title="Learn Testing",
        description="Pytest & FastAPI + TestClient",
        priority=PriorityEnum.MEDIUM
    )
    db_session.add(task)
    db_session.commit()
    db_session.refresh(task)
    yield task
