from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Concrete Strategies
class CreditCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


class DebitCardPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Debit Card.")


class UPIPayment(PaymentStrategy):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")


# Context Class
class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


# Main Program
amount = float(input("Enter payment amount: "))

print("\nChoose Payment Method")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")

choice = int(input("Enter your choice: "))

if choice == 1:
    strategy = CreditCardPayment()
elif choice == 2:
    strategy = DebitCardPayment()
elif choice == 3:
    strategy = UPIPayment()
else:
    print("Invalid Choice")
    exit()

processor = PaymentProcessor(strategy)
processor.make_payment(amount)
