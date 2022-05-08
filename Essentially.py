class Split:

    def __init__(self,numbers=any):
        self.numbers = numbers


    def splitNumber(self):
        digits = [int(x) for x in str(self.numbers)]
        return digits

    

   