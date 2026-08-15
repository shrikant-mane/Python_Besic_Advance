# class BankUser:
#     def __init__(self, name, age):
#         self._name = name
#         self.age =age
#
#     def info(self):
#         print(f"{self._name}")
#         print(f"{self.age}")
#
#
# user = BankUser("shrikant", 27)
# user.info()
# user.name = "vinay"
# user.info()



class BankAccount:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def info(self):
        print(f"{self._name}")
        print(f"{self._balance}")

    def deposit(self, amount):
        self._balance += amount
        print(f"{self._balance}")

    def withdraw(self, amount):
        self._balance -= amount
        print(f"{self._balance}")

    def balance(self):
        print(f"{self._balance}")


bank_account = BankAccount("shrikant", 10000)

bank_account.info()
bank_account.deposit(1000)
bank_account.withdraw(5000)
bank_account.balance()