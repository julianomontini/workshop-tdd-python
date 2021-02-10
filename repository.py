from abc import ABC, abstractmethod
from model import BankAccount

class AbstractBankAccountRepository(ABC):

    @abstractmethod
    def save(self, bank_account: BankAccount) -> BankAccount:
        pass

    @abstractmethod
    def get(self, name: str) -> BankAccount:
        pass

class FakeBankAccount(AbstractBankAccountRepository):
    def __init__(self):
        self.db = {}

    def save(self, bank_account: BankAccount) -> BankAccount:
        self.db[bank_account.name] = bank_account
        return bank_account

    def get(self, name: str) -> BankAccount:
        return self.db.get(name, None)