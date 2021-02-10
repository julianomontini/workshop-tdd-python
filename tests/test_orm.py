from sqlalchemy.orm import Session
from model import BankAccount
import pytest


def test_should_save_bank_account_correctly(session: Session):
    bank_account = BankAccount('Juliano')
    session.add(bank_account)
    session.commit()

    result = session.execute('SELECT id, name, balance FROM bank_accounts').fetchone()
    assert result[0] > 0
    assert (result[1], result[2]) == ('Juliano', 0)

def test_should_retrieve_bank_account_correctly(session: Session):
    session.execute(
        'INSERT INTO bank_accounts(name, balance) VALUES '
        '("JulianoV2", 100)'
    )
    session.commit()

    result: BankAccount = session.query(BankAccount).filter_by(name='JulianoV2').one()
    assert result.name == 'JulianoV2'
    assert result.balance == 100