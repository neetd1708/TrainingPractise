# #OOPS Questions
#
# class Vehicle:
#     max_speed: int = 0
#     mileage: int = 0
#
#     def __init__(self, speed=0, mileage=0):
#         self.max_speed = speed
#         self.mileage = mileage
#
#
# print(Vehicle)
#
# obj1 = Vehicle()
# print(obj1)
#
# buggati = Vehicle(400,0.4)
#
#
# print(buggati)
# print(buggati.max_speed)
# print(buggati.mileage)
#
#
# vehicle1 = Vehicle(250, 18)
#
#
# print(vehicle1)
#
#
#
# class Rectangle:
#     length = 0
#     breadth = 0
#     def __init__(self, l,b):
#         self.length = l
#         self.breadth = b
#
#     def area(self):
#         print(self.length * self.breadth)
#
#     def perimeter(self):
#         print(2*(self.length+self.breadth))
#
# field = Rectangle(10,4)
#
# field.area()
# field.perimeter()
#
# class BankAccount:
#     balance:int
#
#     def __init__(self,b):
#         self.balance = b
#
#     def deposit(self,amount):
#         self.balance += amount
#         print(f"Balance after deposit: {self.balance}")
#
#     def withdraw(self,amount):
#         remaining_balance = self.balance-amount
#
#         if remaining_balance<0:
#             print("Withdrawl not allowed. Insufficient funds")
#         else:
#             self.balance -=amount
#             print(f"Balance after withdrawal: {self.balance}")
#     def printbalance(self):
#         print(f"The balance is:{self.balance}")
#
# cust1 = BankAccount(1000)
#
# cust1.printbalance()
# cust1.deposit(1500)
# cust1.printbalance()
# cust1.withdraw(2000)
# cust1.printbalance()
# cust1.withdraw(1000)
#
#
#
#
# class Light:
#     status:bool
#     def __init__(self,s):
#         self.status = s
#     def turn_on(self):
#         self.status = True
#         print("Light is turned ON")
#     def turn_off(self):
#         self.status = False
#         print("Light is turned OFF")
#     def state(self):
#         if self.status:
#             print("Light is ON")
#         else:
#             print("Light is OFF")
#
# switch1 = Light(True)
#
# switch1.turn_on()
# switch1.state()
# switch1.turn_off()
# print(switch1.status)
# switch1.state()
# switch1.turn_on()
#
#
# class User:
#     username: str
#     __password: str
#
#     def __init__(self,u,p):
#         self.username = u
#         self.__password = p
#
#     def check_password(self, u,p):
#         if self.username==u and self.__password==p:
#             print("Password Correct")
#             return True
#         else:
#             print("Password incorrect")
#             return False
#
# u1 = User("alice", "secure123")
# u2 = User("pat", "nbv123")
#
# print(u1.username)
# u1.check_password("alice","secure123")
# #print(u1.__password)
#
#
# class Vehicle2:
#     colour:str="white"
#
#     def __init__(self, name, top_speed):
#         self.name = name
#         #self.colour = colour
#         self.top_speed = top_speed
#
#     def details(self):
#         print(f"Name:{self.name}, Colour:{self.colour}, Top Speed:{self.top_speed}")
#
#     def seating_capacity(self,capacity):
#         print(f"{self.name} Seating Capacity is:{capacity}")
#
#
#
# v1 = Vehicle2("Tesla", 250)
# v2 = Vehicle2("BMW", 200)
#
# v1.details()
# v2.details()
#
# Vehicle2.colour = "Red"
#
# v1.details()
# v2.details()
#
#
#
# class Bus(Vehicle2):
#
#     def seating_capacity(self):
#         super().seating_capacity(100)
#
#
# bus1 = Bus("vrl travels",120)
#
# print(bus1.details())
# bus1.seating_capacity()
#
# class VehiclesForHire:
#     def __init__(self,base_fare):
#         self.base_fare = base_fare
#
# class Taxi(VehiclesForHire):
#     #def __init__(self,base_fare):
#     #    super().__init__(base_fare)
#     #    self.maintenance_fee = base_fare * 0.10
#     def __init__(self,base_fare):
#         super().__init__(base_fare)
#         self.maintenance_fee = base_fare * 0.10
#
#     def total_fare(self):
#         print(f"Total fare is: {self.base_fare + self.maintenance_fee}")
#
# taxi1 = Taxi(10000)
# print(taxi1.maintenance_fee)
# taxi1.total_fare()
#
#
#
# class Animal:
#     def speak(self,sound):
#         print(f"Animal says :{sound}")
#
#
# class Dog(Animal):
#     def __init__(self,sound="woof"):
#         self.sound = sound
#
#     def speak(self):
#         super().speak(self.sound)
#
# class Cat(Animal):
#     def __init__(self,sound="meow"):
#         self.sound = sound
#
#     def speak(self):
#         super().speak(self.sound)
#
# tommy = Dog()
# tacky = Cat()
#
# tommy.speak()
# tacky.speak()
#
#
# class Animal2:
#     def speak(self,sound):
#         print(f"Animal sound")
#
#
# class Dog2(Animal2):
#     def speak(self):
#         print("Woof")
#
# class Cat2(Animal2):
#     def speak(self):
#         print("Meow")
#
# tommy2 = Dog2()
# tacky2 = Cat2()
#
# tommy2.speak()
# tacky2.speak()
#
#
#
# class Employee:
#     company_name:str = ""
#
#     def __init__(self,name,department="general"):
#         self.name = name
#         self.department = department
#
#
# class FullTimeEmployee(Employee):
#     def __init__(self,name,salary):
#         super().__init__(name)
#         self.salary = salary
#
# class PartTimeEmployee(Employee):
#     def __init__(self,name,hourly_rate,hours):
#         super().__init__(name)
#         self.salary = hourly_rate * hours
#
# emp1 = FullTimeEmployee("Alice", 60000)
# emp2 = PartTimeEmployee("Bob", 500, 20)
#
# print(emp1.salary)
# print(emp2.salary)
#
#
# class Shape:
#     def area(self):
#         return 0
#
# class Circle(Shape):
#     pi = 3.14
#     def __init__(self,radius):
#         self.radius = radius
#
#     def area(self):
#         return self.pi* (self.radius**2)
#
# class Square(Shape):
#     def __init__(self,side):
#         self.side = side
#
#     def area(self):
#         return self.side**2
#
#
# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height
#
#     def area(self):
#         return 0.5 * self.base * self.height
#
# c = Circle(7)
# print(c.area())
# s = Square(10)
# print(s.area())
# t = Triangle(2,8)
# print(t.area())
#
# shapes = [Circle(7), Square(4), Triangle(6, 8)]
# for shape in shapes:
#     print(f"{type(shape).__name__} area: {shape.area()}")
#

class Solution:

    def reverseInGroups(self, arr, k):
        """code here"""
        result = []
        l = len(arr)
        index = 0
        while((l-index)>k):
            result += reversed(arr[index:k])
            index += k
        result += reversed(arr[index:])
        return result

a = Solution()
print(a.reverseInGroups([1, 2, 3, 4, 5],3))

