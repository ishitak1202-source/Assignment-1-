# Different Strategies
class CreditCardPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class PayPalPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")


class UPIpayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


# Context Class
class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


# -------- Main Program --------
print("Select Payment Method")
print("1. Credit Card")
print("2. PayPal")
print("3. UPI")

choice = int(input("Enter Choice: "))
amount = int(input("Enter Amount: "))

if choice == 1:
    processor = PaymentProcessor(CreditCardPayment())
elif choice == 2:
    processor = PaymentProcessor(PayPalPayment())
elif choice == 3:
    processor = PaymentProcessor(UPIpayment())
else:
    print("Invalid Choice")
    exit()

processor.make_payment(amount)




#OUTPUT

Select Payment Method
1. Credit Card
2. PayPal
3. UPI
Enter Choice: 3
Enter Amount: 500

Paid ₹500 using UPI
