from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

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

class AlchemyBankAccountRepository(AbstractBankAccountRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, bank_account: BankAccount) -> BankAccount:
        self.session.add(bank_account)
        self.session.commit()
        return bank_account

    def get(self, name: str) -> BankAccount:
        return self.session.query(BankAccount).filter_by(name=name).first()

class CsvBankAccountRepository(AbstractBankAccountRepository):
    def __init__(self):
        self.base_path = '/Users/julianomontini/PycharmProjects/tdd-1/file_database'

    def _bank_acc_to_csv(self, bank_account: BankAccount) -> str:
        return f'{bank_account.name},{bank_account.balance}'

    def _csv_to_bank_acc(self, csv: str) -> BankAccount:
        name, balance = csv.split(',')
        balance = int(balance)
        return BankAccount(name, balance)

    def _get_file_name(self, account_name: str) -> str:
        return self.base_path + f'/{account_name}.csv'

    def save(self, bank_account: BankAccount) -> BankAccount:
        file_name = self._get_file_name(bank_account.name)
        with open(file_name, 'w') as file:
            file.write(self._bank_acc_to_csv(bank_account))
        return bank_account

    def get(self, name: str) -> BankAccount:
        file_name = self._get_file_name(name)
        try:
            with open(file_name) as file:
                for line in file:
                    return self._csv_to_bank_acc(line)
        except OSError:
            return None