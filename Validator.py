from Essentiallies import Splits,Counts

class sumNumbers(Counts):

    def __init__(self,numbers):
        self.numbers = numbers
        self.ess = Splits(self.numbers)
        self.sortNumber = self.ess.splitNumber()
        self.countOddArray= self.countTotalArrayOdd(self.sortNumber)
        self.countEvenArray= self.countTotalArrayEven(self.sortNumber)
        self.even= 0
        self.odd=0
        
        
    def sumOdd(self):
        for i in range (0,self.countOddArray):
            j=self.countOdd(i)
            self.odd+= int(self.sortNumber[j])
        return self.odd




    def sumEven(self):

        for i in range(0,self.countEvenArray):
            j=self.countEven(i)

            multiplicacion = int(self.sortNumber[j]) *2

            while multiplicacion > 9:
                multiplicacion -=9

            self.even += multiplicacion

        return self.even


    def popArray(self):
        self.sortNumber.pop(-1)
        return int(self.ess.splitUndoNumber(self.sortNumber))


    def answerValidate(self):
            cedula = self.sumEven()+self.sumOdd()

            while cedula > 9:
                cedula -=10

            if cedula == 0:
                return cedula
            
            return 10 - cedula

