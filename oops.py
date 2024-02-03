#object oriented programming
# class students:
#     def __init__(self,name,age,qualification):
#         self.name=name
#         self.age=age
#         self.qualification=qualification
#     def display_name(self):
#         print(self.name)
#     def display_qualification(self):
#         print(self.qualification)
# obj1=students(name="reshi",age="23",qualification="MCA")
# obj1.display_name()
# obj1.display_qualification()

# def students(name,age,qualification):
#     return age
# obj=students("reshi","23","MCA")
# print(obj)

#1.abstraction
#2.encapsulation
#3.inheritance
#4.polymorphisam

# class vehicle:
#     def __init__(self,type,year,company,fuel):
#         self.type=type
#         self.year=year
#         self.company=company
#         self.fuel=fuel
#     def display(self):
#         print("type is",self.type,",year of the production is",self.year,",company name",self.company,",and fuel type is",self.fuel)
#     def company_and_type(self):
#         print(self.company,",",self.type)
#     def fuel_and_company(self):
#         print(self.fuel,",",self.company)

# obj1=vehicle(type="4 wheeler",year="2023",company="range rover",fuel="disel")
# obj1.display()
# obj1.company_and_type()
# obj1.fuel_and_company()

# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area_of_rectangle(self):
#         print("area of rectangle is,",self.length*self.width)
#     def peimeter_of_rectangle(self):
#         print("primeter of rectangle is,",2*(self.length+self.width))
# obj1=rectangle(length=int(input("enter the area of the rectangle")),width=int(input("enter the width of the rectangle")))
# obj1.area_of_rectangle()
# obj1.peimeter_of_rectangle()

# class Book:
#     def __init__(self,title,author,publication_year):
#         self.title=title
#         self.author=author
#         self.publication_year=publication_year
#     def about_of_Book(self):
#         print("the book",self.title,"was authored by",self.author,"and published on",self.publication_year)
# obj1=Book(title=input("enter the title name"),author=input("enter the author name"),publication_year=int(input("enter the year")))
# obj1.about_of_Book()

# class BankAccount:
#     def __init__(self,account_number,balance):
#         self.account_number=account_number
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance=self.balance+amount
#         return self.balance
#     def withdraw(self,amount):
#         if amount>self.balance:
#             return False
#         else:
#             self.balance=amount
#             return self.balance
# obj1=BankAccount(account_number=12345,balance=2000)
# print(obj1.deposit(amount=1000))
# print(obj1.withdraw(amount=1000))

#inheritence

# class Parent:
#     def __init__(self,bike,car):
#         self.bike=bike
#         self.car=car
#     def display(self):
#         return self.car
# class Child(Parent):
#     def show(self):
#         return self.car
    
# obj1=Parent(bike="himalyan",car="range rover")
# print(obj1.display())
# obj2=Child(bike="himalayan",car="fortuner")
# print(obj2.show())    ????

# class parent:
#     def __init__(self):
#         self.car="range rover"
#         self.bike="bullet"
#     def display(self):
#         return self.car
#     def display_bike(self):
#         return self.bike    
# class child(parent):
    # pass  ??

# multi level inheritance

# class vehicle:
#     def info(self):
#         return "used for travel"
# class car(vehicle):
#     pass
# class bike(car):
#     pass
# obj1=bike()
# print(obj1.info())

# multiple inheritence

# class vehicle:
#     def display(self):
#         return "for travel"
# class car:
#     def show(self):
#         return "4 wheel"
# class sports_car(car,vehicle):
#     pass
# obj=sports_car()
# print(obj.display())
# print(obj.show)

# class vehicle:
#     def car(self):
#         print("alto")
#     def bike(self):
#         print("bullet")
# class vehicle_child(vehicle):
#     def bus(self):
#         print("bus")

# obj=vehicle_child()
# obj1=vehicle()
# obj.bike()
# obj.car()
# obj.bus()

# obj1.car()
# obj1.bike()
# obj1.bus()

# class Register:
#     name=str
#     age=int
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.course="python"
#     def reg(self):
#         if self.age>18:
#             return self.name,self.course
#         else:
#             return "get out"
        
# obj=Register(name="hari",age=20)
# print(obj.reg())

# class calculator:
#     n1=int
#     n2=int
#     def __init__(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
#     def add(self):
#         return "addition",self.n1+self.n2
#     def sub(self):
#         return "subration",self.n1-self.n2
#     def mul(self):
#         return "multiplication",self.n1*self.n2
#     def div(self):
#         return "division",self.n1/self.n2
# obj=calculator(n1=2,n2=4)
# print(obj.add())
# print(obj.sub())
# print(obj.mul())
# print(obj.div())

# class Circle:
#     r=int
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         return "area of circle is", 3.14*self.r*self.r
#     def perimeter(self):
#         return "perimeter of circle is",2*3.14*self.r
# obj=Circle(r=2)
# print(obj.area())
# print(obj.perimeter())

# class Person:
#     def __init__(self,name,country,date_of_birth):
#         self.name=name
#         self.country=country
#         self.date_of_birth=date_of_birth
#     def  ???

# class Shoppingcart:
#     def __init__(self,product,price):
#         self.cart={}
#         self.product=product
#         self.price=price
#     def add_cart(self):
#         self.cart[self.product]=self.price
#         return self.cart
#     def remove_cart(self,product):
#         del self.cart[product]
#         return self.cart
#     def total(self):
#         k=sum(self.cart.values())
#         return k
# obj=Shoppingcart(product="p1",price=20)
# print(obj.add_cart())
# print(obj.remove_cart(product="p1"))
# print(obj.total())

# class Person:
#     def __init__(self,name,age,proffession,sex):
#         self.name=name
#         self.age=age
#         self.proffession=proffession
#         self.sex=sex
#     def display_name_age(self):
#         print("My name is",self.name,"and i am",self.age,"yrs old")
#     def display_name_proffession(self):
#         print("My name is",self.name,"and my proffession is",self.proffession)
#     def display_proffession_sex(self):
#         print("My proffession is ",self.proffession,",sex is",self.sex)
#     def display(self):
#         print("My name is",self.name,"and i am",self.age,"old","and my proffession is",self.proffession,",sex is",self.sex)
# obj=Person(name="reshi",age=23,proffession="python full stack developer",sex="Male")
# obj.display_name_age()
# obj.display_name_proffession()
# obj.display_proffession_sex()
# obj.display()

# class Student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def grade(self):
#         if self.marks>=90:
#             return "grade A"
#         elif self.marks>=80 and self.marks<=89:
#             return "grade B"
#         elif self.marks>=70 and self.marks<=79:
#             return "grade C"
#         elif self.marks>=60 and self.marks<=69:
#             return "grade D"
#         elif self.marks<=60:
#             return "grade F"
# obj=Student(name="reshi",age=23,marks=99)
# obj1=Student(name="roshan",age=22,marks=84)
# obj2=Student(name="jithin",age=25,marks=75)
# print(obj.grade())
# print(obj1.grade())
# print(obj2.grade())
# for i in obj,obj1,obj2:
#     print("name:",i.name,",","age:",i.age,",","marks",i.marks,",","grade",i.grade())

# in oops is a langauge feature that allows a subclass or child class to provide a specific implementation od a method that is already provided by one of its superclass or parent class 
class A:
    def func1(self):
        print("functional in class A")
    def func(self):
        print("functional2 in class A")
class B(A):
    def func(self):
        print("function3 in class B")
    def func(self):
        print("functional4 in class B")
        super().func()
        super().func1()
b1=B()

            

 





        




