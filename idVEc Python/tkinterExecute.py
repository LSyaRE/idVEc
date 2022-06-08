from tkinter import Entry, Menu, StringVar, Tk,Label,Button, messagebox,Text
from Essentiallies import Clears,Splits
import webbrowser


from MainDni import MainDni

#Instancias
clear= Clears()
window= Tk()
menuBar =Menu(window)


urlRepository= 'https://github.com/LSyaRE/cedulaObtencion'
urlWebsite= 'https://docslsyare.github.io/idVEc/'


#Funciones
def crearComando():
    return

def validateAnswer(i):
    if i == 'yes':
        return True
    return False 

def ejecutar():
    split = Splits(cedula.get())
    check= len(split.getSplitNumber())
    if check == 9:
        main= MainDni(cedula.get())
        guess=main.guessNumber()
        valorDni.set(f"{guess}")
        entryDni.delete("0","end")
        return 0
    return valorDni.set('Cedula no valida')



def cerrar():
    answer =messagebox.askquestion("Cerrar",message="¿Deseas cerrar la aplicacion?")
    close= validateAnswer(answer)
    if close:
        window.destroy()

def salir():
    answer =messagebox.askquestion("Salir",message="¿Deseas cerrar la aplicacion?")
    close= validateAnswer(answer)
    if close:
        window.destroy()

def versionSoftware():
    messagebox.showinfo("Version",message="Version 0.0.1")

def repositorio():
    webbrowser.open_new_tab(urlRepository)

def website():
    webbrowser.open_new_tab(urlWebsite)

if window.destroy:
    clear.clearCache()

def minimizar():
    window.iconify()



def clearTextInput():
    entryDni.delete("0","end")


#tkinter
window.title("Sistema de cedula")
window.geometry("600x400")
window.resizable(0,0)

#Menu
window.config(menu=menuBar)

archivoMenu= Menu(menuBar, tearoff=0)

# archivoMenu.add_command(label="Nuevo")
# archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Minimizar",command= minimizar)
archivoMenu.add_command(label="Cerrar",command=cerrar)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir",command=salir)

ayudaMenu= Menu(menuBar,tearoff=0)

ayudaMenu.add_command(label="Acerca de",command=website)
ayudaMenu.add_command(label="Repositorio", command=repositorio)
ayudaMenu.add_separator()
ayudaMenu.add_command(label="Version", command=versionSoftware)


menuBar.add_cascade(label="Archivo",menu=archivoMenu)
menuBar.add_cascade(label="Ayuda",menu=ayudaMenu)





#Variables para la cedula 
cedula= StringVar()
cedula.set('')
valorDni= StringVar()
valorDni.set('Ingrese cedula')



tkinterText = Label(window,height=3,font=("Roboto Cn",18) ,text="Bienvenido al sistema de cedula")
tkinterText.pack(padx=10)

dni= Label(window,text="Cedula (9 digitos)").pack()
entryDni= Entry(window,bd=10,textvariable=cedula)
entryDni.pack(pady=10)



sendButton= Button(window,width=15,height=1, text="Enviar", command=ejecutar)
sendButton.pack()

answer= Label(window,text="Respuesta").pack()

answerEntry= Entry(window,bd=30,textvariable=valorDni, state="disable", justify="center" )
answerEntry.pack(pady=20)

answer2= Label(window,text=" Ingrese los primeros nueve digitos.").pack()


window.mainloop()


