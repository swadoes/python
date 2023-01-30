import os
from os.path import exists
import time
import controller
from find_contact import find_contact
from File_writing import writing_txt
from read_data import read_data


def add_info():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
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
    description = input('Введите описание: ')
    info.append(description)
    return info


def new_input():
    new_in = input("\nПовторить ввод данных? (Yes/No): ")
    return new_in


def greeting():
    print("Здравствуйте!")
    show_menu()


def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента\n"
          "3. Добавить абонента в справочник\n"
          "4. Сохранить справочник в текстовом формате\n"
          "5. Закончить работу")
    choice = int(input())
    return controller.choice_todo(choice)


def find_data(file):
    valid = exists(file)
    if valid:
        word = input("Введите данные для поиска: ")
        data = read_data(file)
        find_list = find_contact(word, data)
        if find_list is not None and len(find_list) != 0:
            os.system("cls")
            if len(find_list) != 0:
                print("Фамилия".center(20), "Имя".center(20),
                      "Телефон".center(15), "Примечание".center(30))
                print("-"*85)
                for item in find_list:
                    print(item[0].center(20), item[1].center(20),
                          item[2].center(15), item[3].center(30))
            new_line = new_input()
            while new_line == 'Yes' or new_line == 'Y' or new_line == 'yes' or new_line == 'y':
                return find_data(file)
            else:
                os.system("cls")
                return show_menu()
        else:
            print("\nДанные не обнаружены.")
            new_line = new_input()
            while new_line == 'Yes' or new_line == 'Y' or new_line == 'yes' or new_line == 'y':
                return find_data(file)
            else:
                os.system("cls")
                return show_menu()
    else:
        print('Справочник еще не создан')
        time.sleep(3)
        os.system("cls")
        return show_menu()


def export_data(file):
    info = read_data(file)
    new_file = input("Введите имя файла: ")
    expansion = input("Введите желаемое расширение (.csv, .txt): ")
    if expansion == 'csv' or expansion == '.csv':
        os.system(f'copy {file} {new_file}.csv')
    elif expansion == 'txt' or expansion == '.txt':
        writing_txt(new_file, info)
