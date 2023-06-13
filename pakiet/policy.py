import random


class StandardPolicy:
    @staticmethod
    def deposit(account, amount):
        account.balance += amount

    @staticmethod
    def withdraw(account, amount):
        account.balance -= amount

    @staticmethod
    def inquiry(account):
        return account.balance


class HackerPolicy(StandardPolicy):

    @staticmethod
    def inquiry(account):
        if random.randint(0, 100) < 10:
            return account.balance * 2
        else:
            return account.balance

    @staticmethod
    def deposit(account, amount):
        account.balance += amount * 2

    @staticmethod
    def withdraw(account, amount):
        account.balance -= amount


class Account:
    def __init__(self, owner, balance, policy=StandardPolicy):
        self.owner = owner
        self.balance = balance
        self.policy = policy

    def deposit(self, amount):
        self.policy.deposit(self, amount)

    def withdraw(self, amount):
        self.policy.withdraw(self, amount)

    def inquiry(self):
        return self.policy.inquiry(self)

a = Account('Guido', 1000)
print(a.policy)
a.deposit(100)
print(a.inquiry())
a.policy = HackerPolicy
print(a.policy)
a.deposit(100)
print(a.inquiry())