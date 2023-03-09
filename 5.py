import os
import json

to_save = []

PATH = os.path.dirname(os.path.abspath(__file__))

def fill_ref_dict() -> dict:
    dct = {}
    with open(f'{PATH}/5/reference.txt', 'r') as file:
        for line in file.readlines():
            for char in line:
                if char == '\n': continue
                if char not in dct: dct[char] = 1
                else: dct[char] += 1
        file.close()
    return dict(sorted(dct.items(), key=lambda x:x[1], reverse=True))

def fill_enc_dict() -> dict:
    global to_save
    dct = {}
    with open(f'{PATH}/5/encrypt7.txt', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            to_save.append(line)
            for char in line:
                if char == '\n': continue
                if char not in dct: dct[char] = 1
                else: dct[char] += 1
        file.close()
    return dict(sorted(dct.items(), key=lambda x:x[1], reverse=True))

def save_dict(to_save: dict, filename: str) -> None:
    with open(f'{PATH}/5/{filename}', 'w', encoding='utf-8') as outfile:
        json.dump(to_save, outfile, ensure_ascii=False, indent=4)
        outfile.close()

def save_decode(ref: dict, base: dict) -> None:
    # проверка на вместимость словарей
    with open(f'{PATH}/5/res.txt', 'w', encoding='utf-8') as outfile:
        for line in to_save:
            res_line = ''
            for char in line:
                if char == '\n': res_line += '\n'
                else: res_line += list(ref.keys())[list(base.keys()).index(char)]
            outfile.write(res_line)
        outfile.close()


def main() -> None:
    save_decode(fill_ref_dict(), fill_enc_dict())

if __name__ == '__main__':
    main()