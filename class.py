class avg():
    def __init__(self,name,marks_list):
        self.name=name
        self.marks_list=marks_list

    def avg_mark(self):
        avrg=(self.marks_list[0]+self.marks_list[0]+self.marks_list[0])/3
        return avrg
    @staticmethod
    def hello():
        print(f"hello ")

avrg_sunil=avg("sunil",[2,3,4])
print(avrg_sunil.avg_mark(),avrg_sunil.name)
avrg_sunil.name="aman"
print(avrg_sunil.avg_mark(),avrg_sunil.name)
avrg_sunil.hello()

class account():
    def __init__(self,balance,acc_num):
        self.balance=balance
        self.acc_num=acc_num
    def debit(self,withdraw):
        current_bal=self.balance-withdraw
        self.balance=current_bal
        return self.balance

    def credit(self,deposit):
        current_bal=self.balance+deposit
        self.balance=current_bal
        return self.balance
    def get_balance(self):
        return print("current balance is :",self.balance)

Acc_1=account(3000,8975453628)
print(Acc_1.balance)
Acc_1.debit(200)
Acc_1.credit(700)
print(Acc_1.balance,Acc_1.acc_num)
Acc_1.credit(7800)
Acc_1.get_balance()
##These are interconnected hence easy to maintain single object and same way can make multiple object.
# del keyword will delete the particular attribute of an object

#private attribute
class Account:
    def __init__(self,acc_num,acc_pass):
        self.acc_num=acc_num
        self.__acc_pass=acc_pass
    def inside_access(self):
        print(self.__acc_pass)
##put __ ahead of attribute to make that private,,Also method can also be made private by putting __ahead of it
Client_1=Account("rahman",87687676)
print(Client_1.acc_num)
Client_1.inside_access()## this will be printed
# print(Client_1.__acc_pass)## it will through as inside the class can be accesed but not the outside

##inside classs private function is being used
class Private:
    def __init__(self,name):
        self.name=name

    def __hello(self):
        print("hello")
    
    def welcome(self):
        return print(self.__hello)
Inside_private=Private("aman")
Inside_private.welcome()

"""Abstraction--Show the user that much which is usefull 
Encapsulation--In the class all is present inside and hold all together like a capsule
Inheritance--Take mother qualities and called the class as child class
Multi level inheritance---Class_3--->Class_2--->Class_1-----Class 2 is child of class 2 and Class 3 is child of class 2"""
class Car():
    def __init__(self):
        pass
    @staticmethod
    def start():
        print("car is started")
    @staticmethod
    def stop():
        print("car is stopped")

class Toyota(Car):
    def __init__(self,name):
        self.name=name

class Fortuner(Toyota):
    def __init__(self, fuel):
        self.fuel=fuel
    
    def fuel_type(self):## note you have to write self in the define function
        if self.fuel=="CNG":
            return print("Your car is CNG")
        else: 
            return print("Car is petrol")      
        

Car_1=Toyota("fortuner")
Car_2=Toyota("Harrier")
Car_1.start()## ingeroting property from mother class and object 1
Car_2.stop()## inheriting property from mother class and object 2
Car_3=Fortuner("CNG")##CNG fortuner defined
Car_3.fuel_type()##fuel type method from child class
Car_3.start()## start method from mother of mother class
        
class A():
    varA="welcome to class A"
class B():
    varB="welcome to class B"
class C(A,B):
    varC="welcome to class C"

Var_1=C()
print(Var_1.varC)
print(Var_1.varB)
print(Var_1.varA)

"""Super Method in Inheritance"""
class Car():
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car is started")
    @staticmethod
    def stop():
        print("car is stopped")

class Toyota(Car):
    def __init__(self,name,type):## we can not know the type but in mother we can get it. so we use super method
        super().__init__(type)##now we can access the methop of type frpm parent---see how to call attribute
        self.name=name   
        super().start()  ## it will run the constructor so it will print---see how to call function

C1=Toyota("fortuner","cng")
print(C1.type)


"""Class method--Changes the class attribute"""
"""Static method --do not access any attribute
instance method--normal method--access the self objects"""

class Person:
    name="anonymous"
    def name_change(self,name):
        self.name=name

P1=Person()
P1.name_change("rahman")
print(P1.name)
print(Person.name)## this has not changed the class attribute it has made new attribute
## classmethods help on tyhis

class Person:
    name="anonymous"
    @classmethod
    def name_change(cls,name):## they will take class as default inputs
        Person.name=name

P1=Person()
P1.name_change("rahman")
print(P1.name)
print(Person.name)## both place it has changed now.
##there are other methods as well to do this.


#One way
class Person:
    name="anonymous"
    def name_change(self,name):
        Person.name=name## here start the variable from class

P1=Person()
P1.name_change("rahman")
print(P1.name)
print(Person.name)

#Other way
class Person:
    name="anonymous"
    def name_change(self,name):
        self.__class__.name=name## this will also help change the class attribute

P1=Person()
P1.name_change("rahman")
print(P1.name)
print(Person.name)

"""Propert method--It will automatically change the attribute value which depend on other attribute else we need to do it manualy"""

class Student():
    def __init__(self,math,phy,hindi):
        self.math=math
        self.phy=phy
        self.hindi=hindi
        self.percentage=str((self.math+self.phy+self.hindi)/3)+"%"

percentage=Student(67,87,90)
print(percentage.percentage)
percentage.math=76
print(percentage.percentage)##mit is not updated

##using function
class Student():
    def __init__(self,math,phy,hindi):
        self.math=math
        self.phy=phy
        self.hindi=hindi
    def percentage(self):
        percentage_1=str((self.math+self.phy+self.hindi)/3)+"%"
        return percentage_1

percentage=Student(67,87,90)
print(percentage.percentage())
percentage.math=76
print(percentage.percentage())##automatically changed
## better one is by using propert method when attribute depend on others


class Student():
    def __init__(self,math,phy,hindi):
        self.math=math
        self.phy=phy
        self.hindi=hindi
    @property
    def percentage(self):
        percentage_1=str((self.math+self.phy+self.hindi)/3)+"%"
        return percentage_1

percentage=Student(67,87,90)
print(percentage.percentage)## here we need not to call by () even its a function## it will automatic saves the calculated results
percentage.math=76
print(percentage.percentage)


"""polymorphism---Like + is diffrent meaning for list,int and string"""
a=(1+2)
b=("rahman "+"alam")
c=([1,2,3]+[4,5,6])

##Dunder function use to give these kind of polymorphism to +,- etc,+is not defined for complex number hence we make now
class Complex():
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNum(self):
        print(self.real,"i +",self.img,"j")
    
    def add(self,num2):
        sum_real=(self.real+num2.real)
        sum_img=(self.img+num2.img)
        return Complex(sum_real,sum_img)
    
num1=Complex(1,2)
num1.showNum()
num2=Complex(3,4)
num2.showNum()
num3=num1.add(num2)
num3.showNum()
# num1+num2## this will not work

class Complex():
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNum(self):
        print(self.real,"i +",self.img,"j")
    
    def __add__(self,num2):
        sum_real=(self.real+num2.real)
        sum_img=(self.img+num2.img)
        return Complex(sum_real,sum_img)
    
num1=Complex(1,2)
num1.showNum()
num2=Complex(3,4)
num2.showNum()
 
num3=num1+num2## direct addition possible now
num3.showNum()