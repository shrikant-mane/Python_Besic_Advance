from abc import ABC, abstractmethod

import resource


class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class RazorpayPayment(PaymentGateway):
    def pay(self, amount):
        print(f"Razorpay paid {amount}")
        return True

class CreditCardPayment(PaymentGateway):
    def pay(self, amount):
        print(f"Credit card paid {amount}")
        return True

class StripePayment(PaymentGateway):
    def pay(self, amount):
        print(f"Stripe paid {amount}")
        return True

class OrderService:
    def checkout(self, payment_gateway, amount):
        result = payment_gateway.pay(amount)
        if result:
            print(f"Payment successful")
        else:
            print(f"Payment failed")

payment = RazorpayPayment()
service = OrderService()
service.checkout(payment, 1000)




