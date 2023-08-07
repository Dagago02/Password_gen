import genpassword as modes
import savepass as save
import secrets
import string
import os

mode=0
direction='Pruebas'
#path='C:\\Users\\Daniel Garcia\\Documents\\Programacion\\Repositorios\\Password_gen\\Pruebas' #Directory for saved passwords
path=os.path.abspath(os.getcwd()) + '\\Pruebas'


if mode==1:
    password=modes.genpassword(10)
elif mode==0:
    password=modes.XKCDpassword('_')

save.savepass(password,path,direction)

print(password) 

