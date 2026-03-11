# Classes#
class Student:
    name = "karan"

s1 = Student()
print(s1)


class Car:
    color = "blue"
    brand = "bmw"

car1 = Car()
print(car1.color)
print(car1.brand)


# # init constructor #
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in database")

s1 = Student("shivam", 78)
print(s1.name, s1.marks)
s2 = Student("preeti", 90)
print(s2.name, s2.marks)



# #Question#

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("h1", self.name, "your avg score is:", sum/3)
s1 = Student("tomy", [99, 90, 97])
s1.get_avg()



# # Static methods #
# @class Car:




# Important  

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluch = False

    def start(self):
        self.cluch = True
        self.acc = True
        print("car started")
car1 = Car()
car1.start()





