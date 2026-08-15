from OOPS.process_payment import payment
from excercise.JWT_Token_Validation import payload


class BankUser:
    def __init__(self, name, amount):
        self.name = name
        self._amount = amount

    def account_info(self, payment):
        if self._valid_balance():
            print("Valid account")
        balance = self._calculate_balance(payment)
        print(balance)

    def _valid_balance(self):
        if self._amount > 5000:
            return True

    def _calculate_balance(self, payment):
        result = self._amount - payment
        return result

bank_user = BankUser('Shrikant', 10000)
bank_user.account_info(2000)




