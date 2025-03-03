# A class is a blueprint or template for creating objects and defining methods
# objects - objects is instance of class
#object oriented programming - Object oriented programming is the way to write the well structure and scalable code. there are four principle of object oriented programming.

# 1. Encapsulation
# 2. Abstraction
# 3. Inheritance
# 4. Polymorphism

# 1. Encapsulation

# Encapsulation is the process of bundling data (attributes) and methods into a single unit (class) 
# and restricting access to some attributes using access modifiers.

# Access Modifiers:
# - Private (`__variable`): Accessible only within the class.
# - Protected (`_variable`): Accessible within the class and its subclasses.
# - Public (`variable`): Accessible throughout the code.

from datetime import datetime

class BankManagement:
    def __init__(self):
        """Initialize the bank management system with private, protected, and public attributes."""
        self.__total_amount = 0  # Private variable to store the total balance
        self._account_numbers = ['123A', '123K', '766522B']  # Protected list of account numbers
        self.logs = []  # Public log of transactions

    def check_amount(self):
        """Returns the total amount available in the account."""
        return self.__total_amount

    def get_amount(self, amount, account_number):
        """Withdraws the specified amount from the account if the account number is valid."""
        if account_number in self._account_numbers:
            if self.__total_amount >= amount:
                self.__total_amount -= amount
                transaction = f"{datetime.now()} - Amount: {amount} debited"
                self.logs.append(transaction)
                return transaction
            else:
                return "Insufficient balance"
        else:
            return f"Account number {account_number} is invalid"

    def add_amount(self, amount, account_number):
        """Deposits the specified amount into the account if the account number is valid."""
        if amount > 0 and account_number in self._account_numbers:
            self.__total_amount += amount
            transaction = f"{datetime.now()} - Amount: {amount} credited"
            self.logs.append(transaction)
            return transaction
        else:
            return f"Account number {account_number} is invalid"

    def get_logs(self):
        """Returns the transaction logs."""
        return self.logs


# Testing the BankManagement class
user = BankManagement()

# Depositing money
print(user.add_amount(500, "123A"))  # Expected: Amount credited message
print(user.check_amount())  # Expected: 500

# Checking private attribute access (should give an error)
# print(user.__total_amount)  # Uncommenting this will raise an AttributeError

# Withdrawing money
print(user.get_amount(100, "123A"))  # Expected: Amount debited message
print(user.check_amount())  # Expected: 400

# Checking transaction logs
print(user.get_logs())  # Expected: List of credited and debited transactions




from abc import ABC, abstractmethod

# 1. Abstraction - 
# Abstraction is the process of hiding unnecessary details from the user and exposing only essential features.
# It focuses on what an object does rather than how it does it, simplifying complexity.

# Summary: Why Abstraction?

# Hides Complexity	Users only see what they need.
# Reusability	Same structure can be used for different implementations.
# Maintainability	Changing one part doesn’t break the whole system.
# Loose Coupling	System is more flexible and modular.
# Security	Prevents unwanted access to internal details.


# Abstract base class for Notifications
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        """Abstract method for sending notifications"""
        pass


# Concrete implementation for Email Notification
class EmailNotification(Notification):
    def send(self, message):
        return f"{datetime.now()} - {message} [Email Notification Sent]"


# Concrete implementation for Teams Notification
class TeamsNotification(Notification):
    def send(self, message):
        return f"{datetime.now()} - {message} [Teams Notification Sent]"


# Factory Pattern for creating notifications
class NotificationFactory:
    @staticmethod
    def create_notification(type_: str):
        """Creates and returns a notification instance based on type"""
        if type_ == "email":
            return EmailNotification()
        elif type_ == "teams":
            return TeamsNotification()
        else:
            raise ValueError("Invalid notification type")


if __name__ == "__main__":
    # Creating notifications using the factory pattern
    email_notification = NotificationFactory.create_notification("email")
    print(email_notification.send("Hello, Tomorrow is a holiday!"))

    teams_notification = NotificationFactory.create_notification("teams")
    print(teams_notification.send("Hello, What is today's update?"))
    
    
    
# 🔹 Inheritance in OOP
# Inheritance is one of the fundamental principles of Object-Oriented Programming (OOP). It allows a class (child) to inherit the methods and properties of another class (parent). This promotes code reusability and reduces duplication.

# 🔸 Why Use Inheritance?
# Code Reusability – Avoid rewriting the same code.
# Reduces Redundancy – Define common logic in a base class and reuse it.
# Extensibility – Easily extend existing functionality.
# Maintains Consistency – Follows the DRY (Don’t Repeat Yourself) principle.

# 🔸 Types of Inheritance in Python
# 1 Single Inheritance – One class inherits from another.
# 2️ Multiple Inheritance – A class inherits from multiple parent classes.
# 3️ Multilevel Inheritance – A class inherits from a class that is already inherited.
# 4️ Hierarchical Inheritance – Multiple child classes inherit from the same parent.
# 5️ Hybrid Inheritance – Combination of multiple inheritance types.



class Parent:
    def get_amount(self):
        return 1000
    
    
class child(Parent):
    def __init__(self):
        super().__init__()
        
    def check_balance(self):
        return self.get_amount()
    
    
object = child()
print(object.check_balance())



# Polymorphism is an Object-Oriented Programming (OOP) concept where one interface, method, or function can be used in multiple ways. It allows different objects to respond differently to the same method call.

# Types of Polymorphism
# 1️ Compile-time (Static) Polymorphism – Achieved using Method Overloading (not supported in Python).
# 2️ Runtime (Dynamic) Polymorphism – Achieved using Method Overriding.

#  In Python, we don’t check the object's type; instead, we check if it has the required behavior.


#Method Overloading user *args

class operations:
    def addition(self,*args):
        return sum(args)

    
obj = operations()
print(obj.addition(2,5))
print(obj.addition(2,5,9,0,11))



#Method Overiding

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    
    
class Dog(Animal):
    def make_sound(self):
        return "Bark"   #change or Extend the behavior of class
    
    
class Cat(Animal):
    def make_sound(self):
        return "Meow"
    
    
    

# --------------------------------------------------------------------------------------------------------------
    
    
#MRO - Method Resolution Order

# *MRO defines method inheritence order * in multiple inheritence

#How MRO Works  Orders- 

# 1. Child Class First
# 2. left to right(for multiple inheritance)
# 3. Depth First (Without Repeating Classes) 


class Person:
    def show(self):
        return "I am Person"
        
class Employee(Person):
    def show(self):
        return "I am Employee"
    
    
class Director(Person):
    def show(self):
        return "I am Director"
        
        

obj  = Person()
print(obj.show())
print(Employee.__mro__)    

#--------------------------------------------------------------------------------------------------------------

# Static Method and Class Method @Property

# Static Method (Independent Helper Methods)- It is the method inside the class but does not access of self or cls. it behave like a regular method which logically grouped whithin class.
# usecase - used as helper or utility fuction which does not depend on instane.
# can be called class itself or using instance.
 
 
# Class Methods - (class level methods)  

# When working with class-level data.
# As an alternative constructor to create instances in different ways.
# To modify shared class attributes across all instances.
# For implementing factory methods to return different subclasses dynamically.

class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    @classmethod
    def from_birth_year(cls,name,birth_year):
        return cls(name,datetime.now().year - birth_year)
    
    
obj = Employee("Jon",17)

obj2 = Employee.from_birth_year("ron",1928)

print(obj.__dict__)
print(obj2.__dict__)


# @Property - when you want to restrict direct access from instance varibles
 #Want to Control attribute access  We can implement  
 
class BankManagement:
    def __init__(self):
        self.__Total_amount = 0
        
        
    @property
    def total_amount(self):
        return self.__Total_amount
    
    
    @total_amount.setter
    def total_amount(self,amount):
        if amount < 0:
            raise ValueError("amount can not be negetive!")
        
        self.__Total_amount = amount
        
        
        
bank = BankManagement()

bank.total_amount = 1001
print(bank.total_amount)
    
    
    
    
    
    
    
    

 






        
    
    
    
    
        
        
        
        
        
        
        




