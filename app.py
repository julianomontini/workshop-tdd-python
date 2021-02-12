from flask import Flask, request, jsonify
from factory import ServiceFactory
import service as svc


app = Flask(__name__)

def create_message(message, status_code):
    return jsonify({'message': message}), status_code

@app.route('/users', methods=['POST'])
def create_account():
    user = request.get_json().get('user', None)
    if user is None:
        return create_message('user is a required parameter', 400)

    service = ServiceFactory.bank_account()

    try:
        service.create_account(user)
    except svc.BankAccountAlreadyExistsException:
        return create_message('User already exists', 400)

    return create_message('Success', 201)

@app.route('/transfer', methods=['POST'])
def transfer_money():
    """
    todo: FAZER VALIDACOES E ESCREVER TESTES UNITÁRIOS
    :return:
    """
    source_acc = request.get_json().get('source_account', None)
    target_acc = request.get_json().get('target_account', None)
    amount = request.get_json().get('amount', None)

    service = ServiceFactory.bank_account()

    service.transfer_money(source_acc, target_acc, amount)

    return create_message('Success', 200)