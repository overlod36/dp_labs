import random

OPERATIONS = ["Доступ на чтение", 
              "Доступ на запись", 
              "Передача прав"]

USERS = ['Admin', 'BoJack', 'Dude', 
         'MF Doom', 'Jackson', 'Robert',
         'Lennon', 'Letov', 'Lishenko']

OBJECTS = ['Roland SP-404', 'Boss DR-550', 'Akai MPD 26', 'Zoom SB-246']

matrix = []

def fill_matrix():
    matrix.append(['111' for i in range(len(OBJECTS))])
    for i in range(1, len(USERS)):
        matrix.append([f'{bin(random.randint(0, 7))[2:].zfill(3)}' for j in range(len(OBJECTS))])

def get_str_right(numb: bin) -> str:
    match int(numb, 2):
        case 0:
            return 'Полный запрет'
        case 1:
            return 'Передача прав'
        case 2:
            return 'Запись'
        case 3:
            return 'Запись, Передача прав'
        case 4:
            return 'Чтение'
        case 5:
            return 'Чтение, Передача прав'
        case 6:
            return 'Чтение, Запись'
        case 7:
            return 'Полный доступ'
        case _:
            return 'Неверный аргумент!'


def read(user: str, object_index: int) -> None:
    print('> Операция успешно выполнена!') if matrix[USERS.index(user)][object_index][0] == '1' else print('> Отказ в выполнении операции. У Вас нет прав для ее осуществления!')

def write(user: str, object_index: int) -> None:
    print('> Операция успешно выполнена!') if matrix[USERS.index(user)][object_index][1] == '1' else print('> Отказ в выполнении операции. У Вас нет прав для ее осуществления!')
    

def grant_check(user: str, object_index: int):
    if matrix[USERS.index(user)][object_index][2] == '1': return True
    else: return False

def grant(user: str, to_user: str, right: str, object_index: int):
    if grant_check(user, object_index):
        if right == 'read':
            if matrix[USERS.index(user)][object_index][0] != '1':
                print('> Пользователь не имеет данное право для передачи!')
            else:
                if matrix[USERS.index(to_user)][object_index][0] == '1': print('> Пользователь уже имеет данное право!')
                else: 
                    to_change = list(matrix[USERS.index(to_user)][object_index])
                    to_change[0] = '1'
                    matrix[USERS.index(to_user)][object_index] = ''.join(to_change)
                    print('> Операция успешно выполнена!')
        elif right == 'write':
            if matrix[USERS.index(user)][object_index][1] != '1':
                print('> Пользователь не имеет данное право для передачи!')
            else:
                if matrix[USERS.index(to_user)][object_index][1] == '1': print('> Пользователь уже имеет данное право!')
                else:
                    to_change = list(matrix[USERS.index(to_user)][object_index])
                    to_change[1] = '1'
                    matrix[USERS.index(to_user)][object_index] = ''.join(to_change)
                    print('> Операция успешно выполнена!')
        else:
            print('> Неправильный тип операции!')
    else: print('> Отказ в выполнении операции. У Вас нет прав для ее осуществления!')


def user_auth(user: str):
    return True if user in USERS else False

def user_rights(user: str) -> list:
    return [f'[{OBJECTS[i]}]>  {get_str_right(matrix[USERS.index(user)][i])}' for i in range(len(OBJECTS))]

def user_act(cur_user: str):
    user = cur_user
    while True:
        choice = input(f'[{user}] => ')
        match choice:
            case "rights":
                for el in user_rights(user): print(el)
            case "quit":
                break
            case "read":
                for i in range(len(OBJECTS)): print(f'{OBJECTS[i]} > {i+1}')
                choice = input('> Над каким объектом производится операция? >> ')
                if choice.isnumeric():
                    if 1 <= int(choice) <= 4: read(user, int(choice) - 1)
                    else: print('> Такого объекта нет!')
                else: print('> Введено не число!')
            case "write":
                for i in range(len(OBJECTS)): print(f'{OBJECTS[i]} > {i+1}')
                choice = input('> Над каким объектом производится операция? >> ')
                if choice.isnumeric():
                    if 1 <= int(choice) <= 4: write(user, int(choice) - 1)
                    else: print('> Такого объекта нет!')
                else: print('> Введено не число!')
            case "grant":
                for i in range(len(OBJECTS)): print(f'{OBJECTS[i]} > {i+1}')
                index = int(input('> Над каким объектом производится операция? >> '))
                to_user = input('> Какому пользователю делигируются права? >> ')
                right = input('> Какое право передается? >> ')
                grant(user, to_user, right, index - 1)
            case _:
                print('> Неверная команда!')

def ident():
    while True:
        user = input('[Идентификация] => ')
        if user == 'exit': break
        elif user_auth(user): user_act(user)
        else: print('> Неверный идентификатор!')

            

if __name__ == '__main__':
    fill_matrix()
    ident()
