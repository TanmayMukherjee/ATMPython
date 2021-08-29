class Atm(object):
    def __init__(self,atmCardNumber,pinNumber):
        self.atmCardNumber=atmCardNumber
        self.pinNumber=pinNumber

    def checkBalance(self):
        print("Your Balance is 10000")
    
    
    
    def Withdrawl(self,amount):
        newAmount=10000-amount
        print("Your balance : ",newAmount)


def main():
    cardNumber=input("Enter your Card Number: ")
    pinNumber=input("Enter your Pin Number: ")

    newUser=Atm(cardNumber,pinNumber)
    print("Choose Your Activity")
    print("1.Check Balance 2.Withdrawl")
    activity=int(input("Enter Activity Number: "))
    if(activity==1):
        newUser.checkBalance()
    elif(activity==2):
        amount=int(input("Enter the Amount you want to Withdraw: "))
        newUser.Withdrawl(amount)
    else:
        print("Enter a Valid Number")

main()



