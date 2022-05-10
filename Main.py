from Validator import sumNumbers



#Ultima parte cedula
class MainDni: 
    def __init__(self,numbers):
        self.numbers = numbers
        self.validator = sumNumbers(self.numbers)


    def answerGuess(self):
        cedula = self.validator.sumEven()+self.validator.sumOdd()

        while cedula > 9 and cedula:
            cedula -=10

        if cedula == 0:
            respuesta=cedula
            return respuesta
        
        respuesta = 10 - cedula
        return respuesta
        
    def answerGuess(self):
        cedula = self.validator.sumEven()+self.validator.sumOdd()

        while cedula > 9 and cedula:
            cedula -=10

        if cedula == 0:
            respuesta=cedula
            return respuesta
        
        respuesta = 10 - cedula
        return respuesta





    


