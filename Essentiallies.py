import os
import shutil


# Ayuda a separar los caracteres
class Splits:

    def __init__(self,numbers=any):
        self.numbers = numbers
        self.sentence= ''

    def splitNumber(self):
        digits = [int(x) for x in str(self.numbers)]
        return digits

    def splitUndoNumber(self,words_list):
        for word in words_list:
            self.sentence += str(word)
        return self.sentence



# Even=Pares y Odd=Impares
class Counts:
    def __init__(self):
        pass

    def countOdd(self,i):
        return (i*2)+1

    def countEven(self,i):
        return i*2

    def countArrayOdd(self,i):
        if i == list or tuple or dict:
            j= len(i)
            return int(j/2)
        return 0


    def countArrayEven(self,i):
        if i == list or tuple or dict:
            
            j= len(i)
            j/=2

            if j >= 0.5:
                return round(j+0.1)
    
            return round(j)

        return 0

# elimina algunas cosas
class Clears:
    def __init__(self) -> None:
        pass

    def clearConsole(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  
            command = 'cls'
        return os.system(command)
    
    def clearCache(self):
        if os.path.exists("__pycache__"):
            shutil.rmtree("__pycache__") 
        return 'succesfully remove'
           
















