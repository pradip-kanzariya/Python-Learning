# 9. Object-Oriented Programming (OOP)

# Practice Task : 1 | Create a BankAccount class with deposit and withdrawal methods.
class BankAccount:
    """
    Basic BankAccount class with deposit and withdrawal methods.
    """
    def __init__(self, account_number, account_name, account_balance):
        self.account_number = account_number
        self.account_name = account_name
        self.account_balance = account_balance

    def valid_user(self, acc_name, acc_number):
        if self.account_number == acc_number and self.account_name == acc_name:
            return True
        else:
            return False
    
    def valid_account_number(self, acc_number):
        if self.account_number == acc_number:
            return True
        else:
            return False
        
    def valid_balance(self, money):
        if (self.account_balance - money) >= 0:
            return True
        else:
            return False

    def deposit(self, acc_number, acc_name, money):
        if self.valid_user(acc_name, acc_number):
            self.account_balance += money
            print(f"Account Balance : {self.account_balance}")
        else:
            print("Tansaction fail.")

    def withdrawal(self, acc_number, acc_name, money):
        if self.valid_user(acc_number, acc_name) and self.valid_balance(money):
            self.account_balance -= money
            print(f"Account Balance : {self.account_balance}")
        else:
            print("Tansaction fail.")

    def __str__(self):
        return self.account_name

user = BankAccount(account_number=123, account_name="abc", account_balance=0)
print(user)
user.deposit(acc_number=123, acc_name="abc", money=15)
user.withdrawal(acc_number=123, acc_name="abc", money=20)


# Practice Task : 2 | Build a simple Shape hierarchy with classes for Circle, Square, etc.
class Shape:
    def shape(self):
        print("Shape class shape function.")

class Circle(Shape):
    def shape(self):
        print("Circle is round.")

class Square(Shape):
    def shape(self):
        print("Square shape has 4 equal sides.")

class Triangle(Shape):
    def shape(self):
        print("Triangle shape has 3 sides.")

shapes = [Shape(), Circle(), Square(), Triangle()]
for each_shape in shapes:
    each_shape.shape()