import genpassword as modes
import savepass as save
import os

def Password(mode=0,passlen=10,spacing="_",direction="Default",savepath=os.path.abspath(os.getcwd()) + '\\Pruebas'):

    #direction='Pruebas'
    #path=os.path.abspath(os.getcwd()) + '\\Pruebas'


    if mode==1:
        password=modes.genpassword(passlen)
    elif mode==0:
        password=modes.XKCDpassword(spacing)

    save.savepass(password,savepath,direction)

    print(password) 

