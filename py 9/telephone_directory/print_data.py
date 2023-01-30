import os
from view import show_menu


def print_data(data):
    data.pop(0)
    os.system("cls")
    if len(data) != 0:
        print("Фамилия".center(20), "Имя".center(20),
              "Телефон".center(15), "Примечание".center(30))
        print("-"*85)
        for item in data:
            print(item[0].center(20), item[1].center(20),
                  item[2].center(15), item[3].center(30))
        print(input('\nДля возврата в главное меню нажмите "Ввод"'))
        os.system("cls")
        show_menu()
    else:
        print("Справочник пуст!")
        print(input('\nДля возврата в главное меню нажмите "Ввод"'))
        os.system("cls")
        show_menu()
