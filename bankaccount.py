class User:
    def __init__(self,balance):
        self.balance = balance
        
    
    def make_withdrawal(self,amount):
        self.balance -= amount

    def display_user_balance(self):
        print (self.balance)
    def dep(self,amount):
        self.balance += amount
    def trans(self,amount)
      self.amount

userone =User(500)
userone.dep(33)
userone.dep(33)
userone.dep(33)
userone.make_withdrawal(5)
userone.display_user_balance()

usertoo=User(333)
usertoo.dep(3)
usertoo.dep(3)
usertoo.make_withdrawal(2)
usertoo.make_withdrawal(2)
usertoo.display_user_balance()

userthree=User(1000)
userthree.dep(200)
userthree.make_withdrawal(1)
userthree.make_withdrawal(1)
userthree.make_withdrawal(1)
userthree.display_user_balance()