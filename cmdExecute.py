from Essentiallies import Clears, Splits
from Main import MainDni as main
from colorama import Fore,Style


def clearWorkspace():
    clear.clearConsole()
    clear.clearCache()


try:
    clear=Clears()
    clear.clearConsole()
    print(Fore.LIGHTBLUE_EX+Style.NORMAL+'==================================================')
    print(Fore.WHITE+Style.BRIGHT+'Bienvenidos al sistema de validacion del ultimo numero de la cedula')
    print(Fore.LIGHTBLUE_EX+Style.NORMAL+'==================================================')

    numDni= int(input(Fore.GREEN+'Ingrese su numero de cedula:'+' '))
        
        
    split= Splits(numDni)
    splitNumber=split.splitNumber()
    lenght= len(splitNumber)

 
    if lenght == 9:
        clearWorkspace()
        mainDni = main(numDni)
        hi=mainDni.answer()
        print(Fore.LIGHTBLUE_EX+Style.NORMAL+'==================================================')
        print(Fore.WHITE+Style.BRIGHT+f'Su ultimo numero de cedula es: {Fore.LIGHTGREEN_EX}{hi}')
        print(Fore.LIGHTBLUE_EX+Style.NORMAL+'==================================================')
        print(Fore.WHITE)
        
        
    if lenght == 10:
        clearWorkspace()
        # mainDni = Main.MainDni(numDni)
        # hi=mainDni.answer()
        print(splitNumber[-1])
        if hi == splitNumber[-1]:
            print(Fore.LIGHTBLUE_EX+Style.NORMAL+'==================================================')
            print(Fore.WHITE+Style.BRIGHT+f'Su ultimo numero de cedula es: {Fore.LIGHTGREEN_EX} valida')
            print(Fore.LIGHTBLUE_EX+Style.NORMAL+'==================================================')
        print(Fore.WHITE)
        

except ValueError or lenght >= 11:
        clearWorkspace()
        print(Fore.LIGHTRED_EX+Style.NORMAL+'==================================================')
        print(Fore.RED+Style.BRIGHT+'Ingrese un numero de cedula valida')
        print(Fore.LIGHTRED_EX+Style.NORMAL+'==================================================')
        print(Fore.WHITE)