class InsufficientFoundsException(Exception):
    pass

class BankAccount:
    """
    This class represents the bank account
    """
    def __init__(self, name: str, balance: float = 0):
        self.name = name
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFoundsException()
        self.balance -= amount