from abc import ABC, abstractmethod

# Abstract Base Class
class Animal(ABC):

    def __init__(self, name, age):
        self.name = name
        self._age = age      # Protected Data

    def show_age(self):
        return self._age

    @abstractmethod
    def show_details(self):
        pass


# Child Class 1
class Dog(Animal):

    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def show_details(self):
        print("Dog Name   :", self.name)
        print("Age        :", self.show_age())
        print("Breed      :", self.breed)


# Child Class 2
class Cat(Animal):

    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show_details(self):
        print("Cat Name   :", self.name)
        print("Age        :", self.show_age())
        print("Color      :", self.color)


# -------- Main Program --------
print("----- Dog Information -----")
dog1 = Dog("Bruno", 4, "Golden Retriever")
dog1.show_details()

print("\n----- Cat Information -----")
cat1 = Cat("Kitty", 2, "White")
cat1.show_details()
