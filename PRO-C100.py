class PROC98 :
    def __init__(self,Amount,TypeOfAccount,Pin,Reciept) :
        self.a=Amount
        self.t=TypeOfAccount
        self.p=Pin
        self.r=Reciept

    def moni(self):
        print(self.a)
        print(self.t)
        print(self.p)
        print(self.r)

withraw=PROC98(2000,"Savings",1234,"No Reciept")

withraw.moni()
