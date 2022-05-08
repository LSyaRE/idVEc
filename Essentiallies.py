import os
import shutil


class Splits:

    def __init__(self,numbers=any):
        self.numbers = numbers

    def splitNumber(self):
        digits = [int(x) for x in str(self.numbers)]
        return digits



class Counts:
    def __init__(self):
        pass

    def countOdd(self,i):
        j=(i*2)+1
        return j 

    def countEven(self,i):
        j=i*2  
        return j



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
        return 'remove succesfully'
           
















