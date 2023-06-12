import string
import secrets


#Random Password

alphabet = string.ascii_letters + string.digits + string.punctuation

while True:
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)):
        break

#Password XKCD-style

# On standard Linux systems, use a convenient dictionary file.
# Other platforms may need to provide their own word-list.
with open('top-10000-spanish-words.txt') as f:
    words = [word.strip() for word in f]
    passwordXKCD = '_'.join(secrets.choice(words) for i in range(4))


print(password)
print(passwordXKCD) 