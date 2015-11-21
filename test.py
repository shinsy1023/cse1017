class Test(object):
        def __add__(self, name, num1):
                self.name=name
                self.num=num
                print(self.name+self.num)
                
        def __minus__(self):
                return self.number0-self.number1

test0=Test("3", 4)
test1=Test("5",6)

class BankAccount(object):
        def __init__(self, name, balance):
                self.name=name
                self.balance=balance
                print("A bankn account for", self.name, "is open.")

        def __str__(self):
                return self.name+"'s Bank Account object"

acct1=BankAccount("Yebbuni", 100000)
acct2=BankAccount("Gomdori", 300000)
print("1")
print(acct1)
print(acct2)
