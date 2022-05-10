from Validator import sumNumbers
from Essentiallies import Splits
# Esta parte une todos los modulo0s de la validacion de la cedula y puede ser utilizada 
# por distintas formas graficas 


class MainDni: 
    def __init__(self,numbers):
        self.numbers = numbers
        self.validator = sumNumbers(self.numbers)
        self.split= Splits(self.numbers)
        self.splitNumber=self.split.splitNumber()

        
    
    
    def tenDigits(self):
        self.splitNumber.pop(-1)
        dot=int(self.split.splitUnirNumber(self.splitNumber))
        return dot





    


