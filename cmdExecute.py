from Essentiallies import Clears, Splits
import Main

clear=Clears()
clear.clearConsole()
print('==================================================')
print('Bienvenidos al sistema de validacion del ultimo numero de la cedula')
print('==================================================')

numDni= int(input('Ingrese su numero de cedula excepto el ultimo numero:'+' '))
split= Splits(numDni)
lenght= len(split.splitNumber())



if lenght == 9:
    clear.clearConsole()
    mainDni = Main.MainDni(numDni)
    hi=mainDni.answer()
    print(hi)
    clear.clearCache()
    
else:
    clear.clearConsole()
    print('==================================================')
    print('Ingrese un numero de cedula valida')
    print('==================================================')
    clear.clearCache()