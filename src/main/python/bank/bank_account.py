class BankAccount():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise RuntimeError("Cannot deposit an amount less than or equal to zero")

    def withdraw(self, amount):
        if (self.balance > amount):
            self.balance -= amount
        else:
            print("Insufficient funds!!")

    def statement(self):
        print("Dear {} your account has Rs {}!!".format(self.name, self.balance))
