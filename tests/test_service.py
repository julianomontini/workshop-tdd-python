import pytest

from model import BankAccount, InsufficientFoundsException
from repository import FakeBankAccount
from service import BankAccountService
import service as svc

def get_service():
    repo = FakeBankAccount()
    return BankAccountService(repo), repo

def test_service_should_create_account():
    service, repo = get_service()
    service.create_account('Juliano')
    bank_acc = repo.get('Juliano')
    assert bank_acc.name == 'Juliano'
    assert bank_acc.balance == 0

def test_should_raise_exception_if_username_already_exists():
    service, repo = get_service()
    repo.db['Juliano'] = BankAccount('Juliano')
    with pytest.raises(svc.BankAccountAlreadyExistsException):
        service.create_account('Juliano')

def test_should_raise_exception_if_source_account_doesnt_exist():
    service, repo = get_service()
    service.create_account('Dest')

    with pytest.raises(svc.SourceAccountDoesntExist):
        service.transfer_money('DoesntExist', 'Target', 100)

def test_should_raise_exception_if_target_account_doesnt_exist():
    service, repo = get_service()
    service.create_account('Source')

    with pytest.raises(svc.TargetAccountDoesntExist):
        service.transfer_money('Source', 'Target', 100)

def test_should_not_change_accounts_balance_if_not_enough_founds():
    service, repo = get_service()
    source_acc = service.create_account('Source')
    target_acc = service.create_account('Target')

    source_acc.balance = 50
    target_acc.balance = 25
    repo.save(source_acc)
    repo.save(target_acc)

    with pytest.raises(InsufficientFoundsException):
        service.transfer_money('Source', 'Target', 100)

    source_acc = repo.get('Source')
    target_acc = repo.get('Target')

    assert source_acc.balance == 50
    assert target_acc.balance == 25

def test_should_tranfer_founds():
    service, repo = get_service()
    source_acc = service.create_account('Source')
    target_acc = service.create_account('Target')

    source_acc.balance = 50
    target_acc.balance = 25
    repo.save(source_acc)
    repo.save(target_acc)

    service.transfer_money('Source', 'Target', 10)

    source_acc = repo.get('Source')
    target_acc = repo.get('Target')

    assert source_acc.balance == 40
    assert target_acc.balance == 35