import os
import shutil

#Splits
# This Class returns numbers converted on Arrays and returns Arrays converted on numbers.
class Splits:

    def __init__(self,numbers=any):
        self.numbers = numbers
        self.sentence= ''

    def splitNumber(self):
        return [int(x) for x in str(self.numbers)]

    def splitUndoNumber(self,words_list):
        for word in words_list:
            self.sentence += str(word)
        return int(self.sentence)



class Arrays:
    def __init__(self,array):
        self.array = array


# Counts
class Counts:
    def __init__(self):
        pass

    def countOdd(self,i):
        return (i*2)+1

    def countEven(self,i):
        return i*2

    def countTotalArrayOdd(self,i):
        if i == list or tuple or dict:
            j= len(i)
            return int(j/2)
        return 0

    def countTotalArrayEven(self,i):
        if i == list or tuple:
            j= len(i)
            j/=2
            if j >= 0.5:
                return round(j+0.1)
            return round(j)
        return 0




#Clears
#Delete Cache, console, or other types of documents.
#Syntax to call: nameVariable=Clears(); nameVariable.clearConsole() or  nameVariable.clearCache(); without an argument 
class Clears:
    def __init__(self):
        self.command = 'clear'

    def clearConsole(self):
        if os.name in ('nt', 'dos'):  
            self.command = 'cls'
        return os.system(self.command)
    
    def clearCache(self):
        if os.path.exists("__pycache__"):
            return shutil.rmtree("__pycache__") 
        
           
















