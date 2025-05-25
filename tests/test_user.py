import pytest
from db import SessionLocal, engine
from models import Base, User

@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_user():
    session = SessionLocal()
    user = User(name="Alice")
    session.add(user)
    session.commit()

    fetched = session.query(User).filter_by(name="Alice").first()
    assert fetched is not None
    session.close()
    
