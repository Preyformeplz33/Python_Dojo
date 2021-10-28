class User:
    account = []
    def __init__(self,balance):
        self.balance = balance
        self.int_rate = 0.02
        User.account.append(self)
    def dep(self,amount):
        self.balance += amount
        return self

    def make_withdrawal(self,amount):
        if(self.balance-amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds:Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(self.balance)  #print(f"Balance:{self.balance}")
        return(self)
    
    def yield_interest(self):
        # self.balance+=(self.balance*self.int_rate)#times by a decimal gets you a smaller number
        self.balance=self.balance+self.balance*self.int_rate
        return(self)

    @classmethod
    def we_call_cls(cls):
        for account in cls.account:
            account.display_account_info()

userone = User(500)
userone.dep(3).dep(3).dep(3).make_withdrawal(33).yield_interest().display_account_info()
userone.display_account_info()
userone.yield_interest()
userone.display_account_info()









usertoo = User(333)
usertoo.dep(10).dep(10).make_withdrawal(3).make_withdrawal(3).make_withdrawal(4).make_withdrawal(8).yield_interest().display_account_info()


User.we_call_cls()



