from Essentiallies import Splits,Arrays

class sumNumbers:

    def __init__(self,numbers):
        self.numbers = numbers
        self.ess = Splits(self.numbers)
        self.splitNumber = self.ess.getSplitNumber()
        self.lenghtNumber= len(self.splitNumber)
        self.arrays= Arrays(self.splitNumber)
        self.even= 0
        self.odd=0
        
        
    def __sumOdd(self):
        for i in range (1,self.lenghtNumber,2):
            self.odd+= int(self.splitNumber[i])
        return self.odd


    def __sumEven(self):

        for i in range(0,self.lenghtNumber+1,2):
            multiplicacion = int(self.splitNumber[i])*2
            
            while multiplicacion > 9:
                multiplicacion -=9

            self.even += multiplicacion

        return self.even


    def popArray(self):
        return self.arrays.getArrayPopLastNumber()


    def getValidate(self):
            cedula = self.__sumEven()+self.__sumOdd()

            while cedula > 9:
                cedula -=10
            
            return cedula if cedula == 0 else 10 - cedula
            
           
