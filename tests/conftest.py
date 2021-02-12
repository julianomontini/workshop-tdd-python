from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
import orm
import pytest
from factory import ServiceFactory

@pytest.fixture()
def session_factory():
    engine = create_engine('sqlite://')
    orm.metadata.create_all(engine)

    orm.start_mappers()

    yield sessionmaker(bind=engine)

    clear_mappers()

@pytest.fixture()
def session(session_factory):
    return session_factory()

@pytest.fixture()
def e2e_session():
    yield ServiceFactory.get_session()
    clear_mappers()