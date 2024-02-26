import random
import string

def Generate_pass(length=12):
    password = ''
    chars = strings.acscii_letters + string.digits + string.punctuation
    for i in range(length):
        password += random.choice(chars)

    return password

print('Your password is',Generate_pass)