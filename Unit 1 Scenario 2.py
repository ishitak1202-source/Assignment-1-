# Mobile Store Management System

class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    # Categorize mobile
    def category(self):
        if self.price >= 50000:
            return "Premium"
        elif self.price >= 20000:
            return "Mid-range"
        else:
            return "Budget"


class Store:
    def __init__(self):
        self.mobiles = []

    # Add mobile
    def add_mobile(self, mobile):
        self.mobiles.append(mobile)

    # Display all mobiles
    def display_mobiles(self):
        print("\n----- Mobile Store -----")
        for mobile in self.mobiles:
            print("Brand    :", mobile.brand)
            print("Model    :", mobile.model)
            print("Price    : ₹", mobile.price)
            print("Category :", mobile.category())
            print("------------------------")


# Main Program
store = Store()

n = int(input("Enter number of mobiles: "))

for i in range(n):
    print(f"\nEnter details of Mobile {i+1}")
    brand = input("Brand: ")
    model = input("Model: ")
    price = float(input("Price: "))

    mobile = Mobile(brand, model, price)
    store.add_mobile(mobile)

store.display_mobiles()
