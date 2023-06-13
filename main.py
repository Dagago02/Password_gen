import genpassword as modes
import savepass as save
import secrets
import string
import os

s=0
path=os.getcwd() #Directory for saved passwords

if s==1:
    password=modes.genpassword(10)
elif s==0:
    password=modes.XKCDpassword('_')

save.savepass(password,path,'pruebas')

print(password) 

