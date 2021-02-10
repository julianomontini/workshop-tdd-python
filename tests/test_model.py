from model import BankAccount, InsufficientFoundsException
import pytest

def get_bank_account():
    return BankAccount('Juliano')

def test_constructor_should_set_bank_account_name():
    acc = get_bank_account()
    assert acc.name == 'Juliano'

def test_constructor_should_set_bank_account_to_zero_if_none_is_passed():
    acc = get_bank_account()
    assert acc.balance == 0

def test_deposit_should_increment_the_balance():
    acc = get_bank_account()
    acc.deposit(100)

    assert acc.balance == 100

def test_consecutive_deposits_should_increment_the_balance():
    acc = get_bank_account()
    acc.deposit(100)
    acc.deposit(50)

    assert acc.balance == 150

def test_withdraw_should_decrement_the_balance():
    acc = get_bank_account()
    acc.balance = 50

    acc.withdraw(25)

    assert acc.balance == 25

def test_withdraw_more_founds_that_account_has_should_raise_exception():
    acc = get_bank_account()
    acc.balance = 50

    with pytest.raises(InsufficientFoundsException):
        acc.withdraw(100)