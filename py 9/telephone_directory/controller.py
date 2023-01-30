import os
from read_data import read_data
from print_data import print_data
from File_writing import *
from view import *

file = 'Phonebook.csv'


def beginning():
    greeting()


def choice_todo(n):
    if n == 1:
        data = read_data(file)
        print_data(data)
    elif n == 2:
        find_data(file)
    elif n == 3:
        input_data(file)
        info = add_info()
        writing_scv(file, info)
        new_line = new_input()
        while new_line == 'Yes' or new_line == 'Y' or new_line == 'yes' or new_line == 'y':
            return choice_todo(3)
        else:
            os.system("cls")
            return show_menu()
    elif n == 4:
        export_data(file)
        return show_menu()
    elif n == 5:
        return exit(print("\nВы завершили программу"))
    else:
        os.system("cls")
        return show_menu()
