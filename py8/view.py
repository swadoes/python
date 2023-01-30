import os
from os.path import exists
import time
import controller
from with_data import find_column, find_contact, print_data, read_data, write_json, writing_txt


def add_info(file):
    info = []
    data = read_data(file)
    id_employee = int(len(data[0]) + 1)
    info.append(id_employee)
    last_name = input('Введите фамилию: ').lower().strip()
    info.append(last_name)
    first_name = input('Введите имя: ').lower().strip()
    info.append(first_name)
    patronymic = input('Введите очество: ').lower().strip()
    info.append(patronymic)
    position = input('Введите должность: ').lower().strip()
    info.append(position)
    phone_number = ''
    valid = False
    while not valid:
        try:
            phone_number = input('Введите номер телефона: ')
            phone_number = int(phone_number)
            valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    info.append(phone_number)
    salary = ''
    valid = False
    while not valid:
        try:
            salary = input('Введите ЗП: ')
            salary = float(salary)
            valid = True
        except:
            print('Тут должны быть цифры')
    info.append(salary)
    return info


def new_input():
    new_in = input("\nПовторить ввод данных? (Yes/No): ")
    return new_in


def greeting():
    print("Здравствуйте!")
    show_menu()


def show_menu() -> int:
    global choice
    print("\n" + "=" * 30)
    print("Выберите необходимое действие\n"
          "1. Найти сотрудника\n"
          "2. Добавить сотрудника\n"
          "3. Удалить сотрудника\n"
          "4. Обновить данные сотрудника\n"
          "5. Экспортировать данные\n"
          "6. Закончить работу\n")
    choice = int(input())
    return controller.choice_todo(choice)


def find_data(file):
    valid = exists(file)
    if valid:
        word = input("Введите данные для поиска: ").lower().strip()
        data, keys = read_data(file)
        find_list, ind = find_contact(word, data)
        if len(find_list) != 0:
            os.system("cls")
            print_data(find_list, keys, 1)
        else:
            print("\nДанные не обнаружены.")
            new_find()
    else:
        print('Справочник еще не создан')
        time.sleep(3)
        os.system("cls")
        return show_menu()


def new_find():
    new_line = new_input()
    while new_line == 'Yes' or new_line == 'Y' or new_line == 'yes' or new_line == 'y':
        return find_data(controller.file)
    else:
        os.system("cls")
        return show_menu()


def export_data(file):
    new_file = input("Введите имя файла: ")
    expansion = input("Введите желаемое расширение (.csv, .txt, .json): ")
    if expansion == 'csv' or expansion == '.csv':
        os.system(f'copy {file} {new_file}.csv')
        print(f'Файл {new_file}.csv создан.')
    elif expansion == 'txt' or expansion == '.txt':
        writing_txt(new_file, file)
    elif expansion == 'json' or expansion == '.json':
        write_json(new_file, file)


def delit_employee(data, keys):
    word = input(
        "\nВыберите сотрудника для удаления, по любому полю: ").lower().strip()
    find_list, row = find_contact(word, data)
    if len(find_list) == 1:
        print_data(find_list, keys, 3)
        temp = " ".join(find_list[0][1:4])
        temp = temp.replace('', '').title()
        new_line = input(
            f'\nПодтвертите удаление сотрудника: {temp} ==> Yes/No: ')
        while new_line == 'Yes' or new_line == 'Y' or new_line == 'yes' or new_line == 'y':
            return row, data, keys
        else:
            os.system("cls")
            return show_menu()

    elif len(find_list) > 1:
        print_data(find_list, keys, 3)
        delit_employee(data, keys)

    else:
        print('Такого сотрудника не существует')
        time.sleep(3)
        os.system("cls")
        return show_menu()


def change_data(data, keys):
    word = input(
        "\nВыберите сотрудника для изменения данных, по любому полю: ").lower().strip()
    find_list, row = find_contact(word, data)
    if len(find_list) == 1:
        print_data(find_list, keys, 4)
        change = input(
            '\nЧто вы хотите изменить(наименование столбца)? ').lower().strip().title()
        change_column, id_keys = find_column(change, keys, find_list)
        new_change = input(
            f'\nНа что вы хотите изменить поле {keys[0][id_keys]}: со значением {change_column.title()}? ==> ').lower().strip()
        temp = " ".join(find_list[0][1:4])
        temp = temp.replace('', '').title()
        new_line = input(
            f'\nПодтвертите изменения данных сотрудника: {temp}\n {keys[0][id_keys]}: {change_column.title()} на {keys[0][id_keys]}: {new_change.title()}\n ==> Yes/No: ').lower().strip()
        while new_line == 'Yes' or new_line == 'Y' or new_line == 'yes' or new_line == 'y':
            data[row][id_keys] = new_change
            return data, keys
        else:
            os.system("cls")
            return show_menu()

    elif len(find_list) > 1:
        print_data(find_list, keys, 4)
        change_data(data, keys)

    else:
        print('Такого сотрудника не существует')
        time.sleep(3)
        os.system("cls")
        return show_menu()
