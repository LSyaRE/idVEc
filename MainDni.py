from Validator import sumNumbers
from Essentiallies import Splits
# Esta parte une todos los modulo0s de la validacion de la cedula y puede ser utilizada 
# por distintas formas graficas 


class MainDni(): 
    def __init__(self,numbers):
        self.numbers = numbers
        self.validator = sumNumbers(self.numbers)
       

        
    def guessNumber(self):
        return self.validator.answerValidate()
    

    def validateNumber(self):
        pop = self.validator.popArray()
        validate= sumNumbers(pop)
        split = Splits(self.numbers)
        return validate.answerValidate() == split.splitNumber()[-1]





    


