import os
import shutil

#Splits
# This Class returns numbers converted on Arrays and returns Arrays converted on numbers.
class Splits:

    def __init__(self,numbers):
        self.numbers = numbers
        self.sentence= ''

    def getSplitNumber(self):
        return [int(x) for x in str(self.numbers)]

    def getSplitUndoNumber(self,words_list):
        for word in words_list:
            self.sentence += str(word)
        return int(self.sentence)



class Arrays(Splits):
    def __init__(self,array):
        self.array = array
        
        
    def getArrayPopLastNumber(self):
        self.array.pop(-1)
        return int(self.splitUndoNumber(self.array))





# Counts
#Returns Odd and Even numbers also returns the total Even and Odd Elements in the array.  
class Counts:
    def __init__(self):
        pass

    def countOdd(self,i):
        return (i*2)+1

    def countEven(self,i):
        return i*2

    def countTotalArrayOdd(self,i):
        return  int(len(i)/2) if i == list or tuple else 0


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


        
           
















