class User:
    def __init__(self,balance):
        self.balance = balance
        
    
    def make_withdrawal(self,amount):
        self.balance -= amount
        return self

    def display_user_balance(self):
        print (self.balance)
    def dep(self,amount):
        self.balance += amount
        return self
    def trans(self,amount,user):
        self.balance += amount 
        user.balance -= amount
        print("transfer complete")
        user.display_user_balance()
        self.display_user_balance()

userone =User(500)
userone.dep(33).dep(33).dep(33)
userone.make_withdrawal(5)
userone.display_user_balance()

usertoo=User(333)
usertoo.dep(3).dep(3)
usertoo.dep(3)
usertoo.make_withdrawal(2).make_withdrawal(2)
usertoo.display_user_balance()

userthree=User(1000)
userthree.dep(200)
userthree.trans(33,userone)
userthree.make_withdrawal(1).make_withdrawal(1).make_withdrawal(1)
userthree.display_user_balance()