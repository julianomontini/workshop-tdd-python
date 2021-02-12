from factory import ServiceFactory


service = ServiceFactory.bank_account()

with open('money_transferences.csv') as file:
    for line in file:
        source, target, amount = line.split(',')
        amount = int(amount)
        print('Transfering money', source, target, amount)
        service.transfer_money(source, target, amount)
        print('Done!')