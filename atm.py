class atm(object):
    def __init__(self,atmCardNumber,pinNumber):
        self.atmCardNumber=atmCardNumber
        self.pinNumber=pinNumber
        

    def CashWithdrawl(self):
        print("you have withdraw ₹1")


    def BalanceEnquiry(self):
        print("your Balance is ₹4000000")

d = atm("6778 6754 4658 7457","7685")

print(d.pinNumber)
print(d.BalanceEnquiry())
