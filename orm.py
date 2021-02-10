from sqlalchemy import Table, Integer, Column, Float, String, MetaData
from sqlalchemy.orm import mapper, relationship

from model import BankAccount

metadata = MetaData()

bank_accounts = Table(
    'bank_accounts',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String),
    Column('balance', Float)
)

def start_mappers():
    mapper(BankAccount, bank_accounts)