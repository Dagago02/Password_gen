import genpassword as modes
import savepass as save
import secrets
import string
import os

mode=0
path='/home/daniel/Documents/password_P/pruebas'#Directory for saved passwords

if mode==1:
    password=modes.genpassword(10)
elif mode==0:
    password=modes.XKCDpassword('_')

save.savepass(password,path,'pruebas')

print(password) 

