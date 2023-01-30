import os
from view import add_info, change_data, delit_employee, export_data, find_data, greeting, new_input, show_menu
from with_data import change_file, input_data, print_data, read_data, remove, writing_scv

file = 'horns_hooves.csv'


def beginning():
    greeting()


# def print_data_id(data, keys, cn):
#     print_data(data, keys, cn)


def choice_todo(cn):
    if cn == 0:
        data, keys = read_data(file)
        print_data(data, keys, cn)
    elif cn == 1:
        find_data(file)
    elif cn == 2:
        input_data(file)
        info = add_info(file)
        writing_scv(file, info)
        new_line = new_input()
        while new_line == 'Yes' or new_line == 'Y' or new_line == 'yes' or new_line == 'y':
            return choice_todo(2)
        else:
            os.system("cls")
            return show_menu()
    elif cn == 3:
        data, keys = read_data(file)
        row, data, keys = delit_employee(data, keys)
        remove(row, data, keys, file)
    elif cn == 4:
        data, keys = read_data(file)
        data, keys = change_data(data, keys)
        change_file(data, keys, file)
    elif cn == 5:
        export_data(file)
        return show_menu()
    elif cn == 6:
        return exit(print("\nВы завершили программу"))
    else:
        os.system("cls")
        return show_menu()
