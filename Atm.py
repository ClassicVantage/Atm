class atm():
    def __innit__(self,CardNumber,PinNumber):
        self.CardNumber=CardNumber
        self.PinNumber=PinNumber
    def BalanceEnquiry(self,Balance):
        self.Balance=1000
        print("Your Balance is :" + Balance)

    def transferSum(self,Balance,TransferAmount,AmountRemaining):
        self.Balance=1000
        self.TransferAmount=TransferAmount
        self.AmountRemaining=Balance-TransferAmount
        print("amount of" +TransferAmount+"has been transferred")
        print(AmountRemaining+ " is left")

class main():
    CardNumber=input("Enter Card Number")
    PinNumber=input("Enter pin number")
    TransferAmount=input("Enter Amount to be transferred")
    Atm=atm()

    Atm.BalanceEnquiry()
    Atm.TransferAmount()