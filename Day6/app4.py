# static method 
# class Laptop:
#     storage_type = "ssd"

#     def __init__(self, RAM, storage):
#         self.RAM = RAM
#         self.storage = storage

#      @classmethod
#      def get_storage_type(cls):
#        print(f"storage type = {cls.storage_type}") 

#     def get_info(self): #instance method
#        print(f"laotop has {self.RAM} RAM & {self.storage} {self.srtorage_type}")

#     @staticmethod 
#     def clac_discount(price, discount):
#       final_price = price - (discount * price / 100)
#       print(f"discounted price = {final_price}")

# l1 = Laptop("16gb", "512gb")

# l1.clac_discount(40000, 10)

'''lass Products:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Products.count += 1
    
    def get_info(self):
        print(f"price of {self.name} is Rs.{self.price}")
    
    @classmethod
    def get_count(cls):
        print(f"total products in store = {cls.count}")



p1 = Products("phone", 10000)
p2 = Products("laptop", 50000)
p3 = Products("pen", 10)

Products.get_count()'''
# Encapsulation
'''class BankAccount:
    def __init__(self, name, balance):
        self.name = name #public
        self.__balance = balance #protected private - data mangling
    def get_balance(self): #gettar
       return self.__balance
    
    def set_balance(self, newBalance): # settars
       self.__balance = newBalance
    
acc1 = BankAccount("Rahul kumar", 10000)


acc1.set_balance(20_0000)
print(acc1.name, acc1.get_balance())'''

# inheritance

'''class Employee:
    start_time = "10am"
    end_time = "6pm"

    def change_time(self, new_end_time):
        self.end_time = new_end_time
class Teacher(Employee): # single level inheritance
    def __init__(self, subjects):
        self.subjects = subjects

t1 = Teacher("Math")
t1.change_time("5pm")

print(t1.subjects, t1.start_time, t1.end_time)'''

# multilevel Inheritance

class Employee:
    start_time = "10am"
    end_time = "6pm"

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

class Accountant(AdminStaff):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary

acc1 = Accountant(25_000, "CA")

print(acc1.role, acc1.salary, acc1.start_time, acc1.end_time)