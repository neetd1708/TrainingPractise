class Employee:
    def set_data(self,n,a,s):
        self.name =n
        self.age=a
        self.salary=s
    def display_data(self):
        print(self.name,self.age,self.salary)

e1=Employee()
e1.set_data('R',23,30000)

e1.display_data()



class Fruit:
    count =0

    def __init__(self,name='',size=0,color=''):
        self.__name=name
        self.__size=size
        self.__color=color
        Fruit.count+=1
    def display():
        print(Fruit.count)

f1 = Fruit('Banana',5,'Yellow')
#print(vars(Fruit))
##print(dir(Fruit))
#print(vars(f1))
#print(dir(f1))



class Number:
    def set_number(self,n):
        self.num = n
    def get_number(self):
        return self.num
    def print_number(self):
        print(self.num)
    def isnegative(self):
        return self.num<0
    def isdivisibleby(self, divisor):
        if self.num%divisor ==0:
            print(f"Divisible by {divisor}")
        else:
            print(f"Not divisible by {divisor}")
    def absolute_value(self):
        return abs(self.num)



x = Number()
x.set_number(19)
z=x.get_number()
print(z)
x.print_number()
print(x.isnegative())
x.isdivisibleby(4)
print(x.absolute_value())