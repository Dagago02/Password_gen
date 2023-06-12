import string
import secrets

def genpassword(n):
    #Random Passwords
    alphabet = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(n))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)):
            break
    return password

def XKCDpassword(str):
    #Password XKCD-style

    with open('top-10000-spanish-words.txt') as f:
       words = [word.strip() for word in f]
       passwordXKCD = str.join(secrets.choice(words) for i in range(4))
    return passwordXKCD

