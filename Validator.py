
from Essentiallies import Splits,Counts

class sumNumbers:

    def __init__(self,numbers):
        self.numbers = numbers
        self.ess = Splits(self.numbers)
        self.sortNumber = self.ess.splitNumber()
        self.counts= Counts()
        
        
    def sumOdd(self):
        
        impares=0
        for i in range (0,4):
            j=self.counts.countOdd(i)
            impares += int(self.sortNumber[j])
        return impares

       
    def sumEven(self):
        impares =0

        for i in range(0,5):
            j=self.counts.countEven(i)

            multiplicacion = int(self.sortNumber[j]) *2

            while multiplicacion > 9:
                multiplicacion -=9

            impares += multiplicacion

        return impares