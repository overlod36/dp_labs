A = 7
K = 3
M = 27
ALPH = ' abcdefghijklmnopqrstuvwxyz'
next_alph = ''

def fill():
    global next_alph
    for symb in ALPH: next_alph += ALPH[(A*ALPH.find(symb) + K) % M]

def encryp(message: str) -> str:
    res = ''
    for symb in message: res += ALPH[next_alph.find(symb)]
    return res

def decryp(message: str) -> str:
    res = ''
    for symb in message: res += ALPH[(A*ALPH.find(symb) + K) % M]
    return res

def menu():
    while True:
        choice = input('> ')
        match choice:
            case 'exit':
                break
            case _:
                res = decryp(choice)
                print(f'Результат шифрования >> {res}')
                print(f'Результат дешифрования >> {encryp(res)}')

if __name__ == '__main__':
    fill()
    menu()