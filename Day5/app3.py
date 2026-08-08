# object oriented programming
'''class Student: 
    # subjects = "python"
    # college = "Abc"
    # year = "4th year"
    def __init__(self, name, cgpa): #parametarized constructor
        self.name = name
        self.cgpa = cgpa
    def get_cgpa(self):
        return self.cgpa

stu1 = Student("Rahul", 9.0)
stu2 = Student("Sajid", 8.4)
stu3 = Student("abid", 9.2)

print(f"{stu1.name}  has cgpa = {stu1.get_cgpa()}")'''

# print(stu1.cgpa)
# print(stu2.name)
# print(stu3.name)

# stu2 = Student()
# print(stu1.subjects, stu1.college, stu1.year)
# print(stu2.subjects, stu2.college, stu2.year)
# l = [1, 2]
# s = set()
# print(type(l))

class Student:
    college_name = "ABC college" #class
    PI = 3.1
    def __init__(self, name, gpa):
        self.name = name #instance
        self.gpa = gpa
        self.PI = 3.14
stu1 = Student("Rahul", 9.2)

# print(stu1.name)
# print(stu1.college_name)
# # print(Student.PI)
# print(stu1.PI)

class Laptop:
    storage_type = "ssd"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage
    
    @classmethod
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")


    def get_info(self): # instance method
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

l1 = Laptop("16gb", "512gb")
# l2 = Laptop("8gb", "256gb")

# l1.get_info()
print(Laptop.get_storage_type)

l1.get_storage_type()