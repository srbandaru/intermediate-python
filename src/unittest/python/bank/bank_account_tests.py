from unittest import TestCase
from bank.bank_account import BankAccount


class TestBankAccount(TestCase):
    def test_deposit(self):
        account = BankAccount("Sameer", 1000)
        account.deposit(500)
        assert account.balance == 1500

    def test_withdraw(self):
        account = BankAccount("Sameer", 1000)
        account.withdraw(100)
        assert account.balance == 900