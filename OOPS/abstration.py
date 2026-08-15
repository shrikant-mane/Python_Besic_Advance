from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    # pass
    def pay(self):
        print("UPI")


class CreditCard(Payment):
    def pay(self):
        print("Credit Card")

upi = UPI()
upi.pay()



class Connection(ABC):

    @abstractmethod
    def db_connection(self):
        pass


class Mysql(Connection):
    def db_connection(self):
        print("Mysql")

class Postgresql(Connection):
    def db_connection(self):
        print("PostgreSQL")

m = Mysql()
m.db_connection()

p = Postgresql()
p.db_connection()

