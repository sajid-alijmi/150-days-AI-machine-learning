# multiple Inheritance

#class Teacher: 
    def __init__(self, salary):
        self.salary = salary

class Student: 
    def __init__(self, gpa):
        self.gpa = gpa
        
class TA(Teacher, Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name

ta1 = TA(15_000, 9.3, "Sajid")

#print(ta1.name, ta1.gpa, ta1.salary)

# Abstract class

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("roar")

class Cow(Animal):
    def make_sound(self):
      print("moo!")

lion = Lion()
lion.make_sound()

cow = Cow()
cow.make_sound()

# Polymorphism
# function overriding
# class Employee:
#     def get_desiganation(self):
#         print("desiganation = Employee")

# class Teacher(Employee):
#     def get_desiganation(self):
#         print("designation = Teacher")

# t1.Teacher()
# t1.get_desiganation()
