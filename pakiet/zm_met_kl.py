import random


class Account:
    num_accounts = 0

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        Account.num_accounts += 1

    @classmethod
    def from_xml(cls, data):
        from xml.etree.ElementTree import XML
        doc = XML(data)
        return cls(doc.findtext("owner"), float(doc.findtext("balance")))

    def __repr__(self):
        return f"Account({self.owner}, {self.balance}), {type(self).__name__}"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def inquiry(self):
        return self.balance


data = '''
<account>
<owner>Marek</owner>
<balance>300043.00</balance>
</account>
'''

a = Account("Guido", 1000.00)
b = Account("Bill", 10.00)
c = Account("Rich", 1000000.00)
d = Account.from_xml(data)
print(d)
print(Account.num_accounts)
print(a.num_accounts)

class HackerAccount(Account):
    def deposit(self, amount):
        self.balance += 2 * amount

    def inquiry(self):
        if random.randint(0, 4) == 1:
            return self.balance * 1.10
        else:
            return self.balance


e = HackerAccount.from_xml(data)
print(e)

