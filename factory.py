from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import create_engine

import orm
from service import BankAccountService
from repository import AlchemyBankAccountRepository, CsvBankAccountRepository

DB_URL = "sqlite:////Users/julianomontini/PycharmProjects/tdd-1/main.db"

class ServiceFactory:
    engine = None

    @classmethod
    def get_session(cls):
        if cls.engine is None:
            cls.engine = create_engine(DB_URL)
            orm.metadata.create_all(cls.engine)
            orm.start_mappers()
        return sessionmaker(bind=cls.engine)()


    @classmethod
    def bank_account(cls) -> BankAccountService:
        session = cls.get_session()
        return BankAccountService(AlchemyBankAccountRepository(session))
        #return BankAccountService(CsvBankAccountRepository())