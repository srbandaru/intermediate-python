from bank.bank_account import BankAccount


class Savings(BankAccount):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.account_type = 'savings'
