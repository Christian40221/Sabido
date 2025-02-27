class Bankaccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

account = Bankaccount("Christian", 5000)

print(account.owner)
account.deposit(1000)
print(account.get_balance())
account.withdraw(500)
print(account.get_balance())
