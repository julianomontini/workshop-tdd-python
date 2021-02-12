from behave import *
import requests
from uuid import uuid4

from factory import ServiceFactory

BASE_URL = "http://localhost:5000"


@given("The {account_type} account exists")
def step_impl(context, account_type):
    user = str(uuid4())

    payload = {
        'user': user
    }

    result = requests.post(BASE_URL + "/users", json=payload)
    assert result.status_code == 201

    if account_type == 'source':
        context.source_acc = user
    else:
        context.target_acc = user

@step("The {account_type} account balance is {acc_balance}")
def step_impl(context, acc_balance, account_type):
    session = ServiceFactory.get_session()

    if account_type == 'source':
        name = context.source_acc
    else:
        name = context.target_acc

    session.execute(
        "UPDATE bank_accounts SET balance = :balance WHERE name = :name",
        {'balance': int(acc_balance), 'name': name}
    )
    session.commit()

@when("I transfer {amount}")
def step_impl(context, amount):
    payload = {
        'source_account': context.source_acc,
        'target_account': context.target_acc,
        'amount': float(amount)
    }

    result = requests.post(BASE_URL + "/transfer", json=payload)
    context.operation_message = result.json()['message']


@then("The {account_type} account balance should be {account_balance}")
def step_impl(context, account_type, account_balance):
    session = ServiceFactory.get_session()

    if account_type == 'source':
        name = context.source_acc
    else:
        name = context.target_acc

    result = session.execute(
        "SELECT balance FROM bank_accounts WHERE name = :name",
        {'name': name}
    ).fetchone()

    assert float(result[0]) == float(account_balance)


@step("The operation message is {message}")
def step_impl(context, message):
    assert context.operation_message == message