import genpassword as modes
import secrets
import string

password=modes.genpassword()
passwordXKCD=modes.XKCDpassword()

print(password)
print(passwordXKCD) 