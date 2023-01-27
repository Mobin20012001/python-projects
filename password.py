import random
char = '0123456789zxcvbnm._lkjhgfdsaqwertyuiopZXCVBNMLKJHGFDSAQWERTYUIOP'

length = int(input('length of your password: '))

print('this is your password: ')

for a in range(length):
    password = random.choice(char)
    print(password,end='')