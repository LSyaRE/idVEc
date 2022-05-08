from Essentially import Split


class Validator:

    def __init__(self,numbers):
        self.numbers = numbers

    def sumImapres(self):
        ess = Split(self.numbers)
        sortNumber = ess.splitNumber()
        j=1
        impares=0
        for i in range (0,4):
            impares += int(sortNumber[j])
            j+=2
        return impares

       
    def sumPares(self):
        ess = Split(self.numbers)
        sortNumber = ess.splitNumber()

        impares =0
        j=0

        for i in range(0,5):
            multiplicacion = int(sortNumber[j]) *2
            j+=2
            while multiplicacion > 9:
                multiplicacion -=9

            impares += multiplicacion

            

        return impares



validator = Validator(1752330769)

cedula = validator.sumPares()+validator.sumImapres()

while cedula > 9 and cedula:
    cedula -=10
    

if cedula == 0:
    respuesta=cedula
else:    
    respuesta = 10 - cedula

print(respuesta)