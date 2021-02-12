from sqlalchemy.orm import Session

from repository import AlchemyBankAccountRepository
from model import BankAccount

def get_repository(session):
    return AlchemyBankAccountRepository(session)

def test_repository_can_save_object(session: Session):
    repo = get_repository(session)

    account = BankAccount('Juliano')
    repo.save(account)

    result = session.execute(
        "SELECT id, name, balance "
        "FROM bank_accounts "
        "WHERE name=:name",
        {'name': 'Juliano'}
    ).fetchone()

    assert result[0] > 0
    assert (result[1], result[2]) == ('Juliano', 0)

def test_repository_can_get_object(session: Session):
    repo = get_repository(session)

    session.execute(
        'INSERT INTO bank_accounts(name, balance) VALUES '
        '("Juliano", 250)'
    )
    session.commit()

    bank_account = repo.get('Juliano')
    assert (bank_account.name, bank_account.balance) == ('Juliano', 250)