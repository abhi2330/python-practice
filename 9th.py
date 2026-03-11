 class Person:
    __name = "anonymous"

    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

p1 = Person()
print(p1.welcome())



#Inheritance methode#

class Car:
    @staticmethod
    def start():
        print("car started...")


    @staticmethod
    def stop():
        print("car stopped")

class TayotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = TayotaCar("fortuner")
car2 = TayotaCar("prius")

print(car1.start)
print(car2.name)