from model import BankAccount
from repository import AbstractBankAccountRepository

class BankAccountAlreadyExistsException(Exception):
    pass
class SourceAccountDoesntExist(Exception):
    pass
class TargetAccountDoesntExist(Exception):
    pass
class AccountDoesntHaveEnoughFoundsException(Exception):
    pass

class BankAccountService:
    def __init__(self, bank_acc_repo: AbstractBankAccountRepository):
        self.bank_acc_repo = bank_acc_repo
    def create_account(self, name: str) -> BankAccount:
        existing_account = self.bank_acc_repo.get(name)
        if existing_account is not None:
            raise BankAccountAlreadyExistsException()
        acc = BankAccount(name)
        self.bank_acc_repo.save(acc)
        return acc
    def transfer_money(self, source_acc_name: str, target_acc_name: str, amount: float):
        source_acc = self.bank_acc_repo.get(source_acc_name)
        if source_acc is None:
            raise SourceAccountDoesntExist()

        target_acc = self.bank_acc_repo.get(target_acc_name)
        if target_acc is None:
            raise TargetAccountDoesntExist()

        source_acc.withdraw(amount)
        target_acc.deposit(amount)

        self.bank_acc_repo.save(source_acc)
        self.bank_acc_repo.save(target_acc)