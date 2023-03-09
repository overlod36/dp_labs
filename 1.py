import random

alph = 'абвгдеёжзийклмнопрстуфхцчшщъьыэюя0123456789'
PASSWORDS_COUNT = 20
PASSWORD_LENGTH = 8

cur_password = ''
passwords_list = []

for i in range(PASSWORDS_COUNT):
    for j in range(PASSWORD_LENGTH):
        cur_password += alph[random.randint(0, len(alph) - 1)]
    passwords_list.append(cur_password)
    cur_password = ''

for password in passwords_list:
    print(f'=> {password}')

wait = input()
