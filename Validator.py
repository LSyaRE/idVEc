
from re import S
from Essentiallies import Splits,Counts

class sumNumbers:

    def __init__(self,numbers):
        self.numbers = numbers
        self.ess = Splits(self.numbers)
        self.sortNumber = self.ess.splitNumber()
        self.counts= Counts()
        self.countOddArray= self.counts.countArrayOdd(self.sortNumber)
        self.countEvenArray= self.counts.countArrayEven(self.sortNumber)
        self.even= 0
        self.odd=0
        
        
    def sumOdd(self):
        for i in range (0,self.countOddArray):
            j=self.counts.countOdd(i)
            self.odd+= int(self.sortNumber[j])
        return self.odd




    def sumEven(self):

        for i in range(0,self.countEvenArray):
            j=self.counts.countEven(i)

            multiplicacion = int(self.sortNumber[j]) *2

            while multiplicacion > 9:
                multiplicacion -=9

            self.even += multiplicacion

        return self.even


