import genpassword as modes
import secrets
import string

password=modes.genpassword(10)

passwordXKCD=modes.XKCDpassword('_')

print(password)
print(passwordXKCD) 