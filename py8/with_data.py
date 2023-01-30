
import os
from os.path import exists
import json
import csv
import time
import view


def input_data(file):
    valid = exists(file)
    if not valid:
        creating_csv(file)


def creating_csv(file):
    with open(file, 'w', encoding='utf-8') as data:
        data.write(
            f'Id,Фамилия;Имя;Очество;Должность;Телефон;Зарплата\n')


def writing_scv(file, info):
    with open(file, 'a', encoding='utf-8') as data:
        data.write(
            f'{info[0]};{info[1]};{info[2]};{info[3]};{info[4]};{info[5]};{info[6]}\n')
    return print("\nЗапись сохранена")


def writing_txt(new_file, file):
    data, keys = read_data(file)
    file = f'{new_file}.txt'
    f = open(file, 'w')
    f.close()
    count = 0
    if count < len(data):
        for _ in data:
            with open(file, 'a', encoding='utf-8') as f:
                f.write(
                    f'{keys[0][1]}: {data[count][1].title()}\n{keys[0][2]}: {data[count][2].title()}\n{keys[0][3]}: {data[count][3].title()}\n{keys[0][4]}: {data[count][4].title()}\n{keys[0][5]}: {data[count][5].title()}\n{keys[0][6]}: {data[count][6].title()}\n\n')
            count += 1
    return print(f'Файл {file} создан.')


def write_json(new_file, file):
    data = {}
    with open(file, encoding='utf-8') as csvf:
        reader = csv.DictReader(csvf, delimiter=';')
        for rows in reader:
            key = rows['Id']
            data[key] = rows
    file = f'{new_file}.json'
    f = open(file, 'w')
    f.close()
    with open(file, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    return print(f'Файл {file} создан.')


def remove(row, data, keys, file):
    with open(file, 'w', encoding='utf-8', newline='') as f:
        write = csv.writer(f, delimiter=';')
        if row != 0:
            write.writerows(keys + data[:row] + data[row + 1:])
        else:
            write.writerows(keys + data[row + 1:])
    return print('Запись удалена'), view.show_menu()


def change_file(data, keys, file):
    with open(file, 'w', encoding='utf-8', newline='') as f:
        write = csv.writer(f, delimiter=';')
        write.writerows(keys + data)
    return print('Запись изменена'), view.show_menu()


def read_data(file):
    valid = exists(file)
    if valid:
        with open(file,  encoding='utf-8', newline='') as file:
            data = []
            reader = csv.DictReader(file, delimiter=';')
            keys = [reader.fieldnames]
            for line in reader:
                temp = []
                for i in line:
                    t = line[i]
                    if t is not None:
                        temp.append(t)

                data.append(temp)

            return data, keys

    else:
        print('Справочник еще не создан')
        time.sleep(3)  # import time
        os.system("cls")
        return view.show_menu()


def print_data(data, keys, ch, indent=1, max_width=120):
    os.system("cls")
    if len(data) is not None:
        max_columns = []
        for col in zip(*data):
            len_el = []
            [len_el.append(len(el)) for el in col]
            max_columns.append(max(len_el))

        max_columns_title = []
        for col in zip(*keys):
            max_columns_title.append(max([len(el) for el in col]))

        for col in keys:
            width = []
            for n, c in enumerate(col):
                if max_columns[n] >= max_columns_title[n]:
                    w = max_columns[n] + indent
                    width.append(w)
                else:
                    w = max_columns_title[n] + indent
                    width.append(w)

                if sum(width) <= max_width:
                    print(f'{c:<{w}}', end='')
                else:
                    print('Ширина таблицы больше допустимого значения')
                    return
            print()

        print(f"{'='*(sum(width))}")

        for el in data:
            for n, col in enumerate(el):
                print(f'{col.title():<{width[n]}}', end='')
            print()

        if ch == 1:
            return view.new_find()
        elif ch == 3:
            return

        elif ch == 4:
            return data, keys

        else:
            print(input('\nДля возврата в главное меню нажмите "Ввод"'))
            os.system("cls")
            view.show_menu()
    else:
        print("Справочник пуст!")
        print(input('\nДля возврата в главное меню нажмите "Ввод"'))
        os.system("cls")
        view.show_menu()


def find_contact(world, data):
    dat = []
    ind = 0
    for i in data:
        # print(world in i)
        if world in i:
            temp = i
            ind = data.index(i)
            dat.append(temp)

    return dat, ind


def find_column(change, keys, find_list):
    id_keys = 0
    for i in keys:
        for j in i:
            if change in j:
                id_keys = i.index(j)
    return find_list[0][id_keys], id_keys
