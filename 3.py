import random

ROOTS = ['NONCONFIDENTIAL', 'CONFIDENTIAL', 'SECRET', 'TOP SECRET']

USERS = ['Admin', 'BoJack', 'Dude', 
         'MF Doom', 'Jackson', 'Robert',
         'Lennon', 'Letov', 'Lishenko']

OBJECTS = ['Roland SP-404', 'Boss DR-550', 'Akai MPD 26', 'Zoom SB-246']

users_storage = { key: None for key in USERS }
objects_storage = { key: None for key in OBJECTS }

def fill_storages() -> None:
    for key in users_storage:
        if key == 'Admin':  users_storage[key] = [len(ROOTS) - 1, len(ROOTS) - 1]
        else:
            to_save = random.randint(0, len(ROOTS) - 1)
            users_storage[key] = [to_save, to_save]
    
    for key in objects_storage:
        objects_storage[key] = random.randint(0, len(ROOTS) - 1)

def print_storages() -> None:
    print('[ Пользователи ]:')
    for key in users_storage:
        print(f'{key} > {ROOTS[users_storage[key][0]]}')
    print('[ Объекты ]:')
    for key in objects_storage:
        print(f'{key} > {ROOTS[objects_storage[key]]}')

def print_objects() -> None:
    for el in OBJECTS: print(f'[{el}]', end=' ')
    print()

def print_roots() -> None:
    for root in ROOTS: print(f'[{root}]', end=' ')
    print()

def check_choice(obj: str) -> bool:
    if not obj.isdigit(): 
        print('> Введено не число!')
        return False
    elif not 1 <= int(obj) <= len(OBJECTS):
        print('> Такого объекта нет!')
        return False
    return True

def read(user : str) -> None:
    print_objects()
    obj = input('> Над каким объектом производится операция? >> ')
    if check_choice(obj):
        if objects_storage[OBJECTS[int(obj) - 1]] <= users_storage[user][0]: print('> Операция чтения успешно выполнена!')
        else: print('> Операция чтения отклонена!')

def write(user: str) -> None:
    print_objects()
    obj = input('> Над каким объектом производится операция? >> ')
    if check_choice(obj):
        if objects_storage[OBJECTS[int(obj) - 1]] >= users_storage[user][0]: print('> Операция записи успешно выполнена!')
        else: print('> Операция записи отклонена!')
    
def change(user: str) -> None:
    print_roots()
    root = input('> Введите уровень безопасности >> ')
    if root not in ROOTS: print('> Такого уровеня безопасности нет!')
    else:
        if ROOTS.index(root) <= users_storage[user][1]:
            users_storage[user][0] = ROOTS.index(root)
            print('> Операция изменения уровня безопасности выполнена!')
        else: print('> Изменение уровня безопасности невозможна!')

def user_ident(user: str) -> bool:
    return True if user in USERS else False

def user_act(cur_user: str) -> None:
    user = cur_user
    while True:
        choice = input(f'[{user}] => ')
        match choice:
            case 'read': read(user)
            case 'write': write(user)
            case 'change': change(user)
            case 'print': print_storages()
            case 'quit': break
            case _: print('> Неверная команда!')

def ident() -> None:
    while True:
        user = input('[Идентификация] => ')
        if user == 'exit': break
        elif user_ident(user): user_act(user)
        else: print('> Неверный идентификатор!')

if __name__ == '__main__':
    fill_storages()
    ident()