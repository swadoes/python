import os
import csv
from os.path import exists
import time
import controller


def read_data(file):
    valid = exists(file)
    if valid:
        with open(file,  encoding='utf-8') as file:
            data = []
            reader = csv.reader(file, delimiter=";")
            for line in reader:
                temp = f'{" ".join(line)}'.strip().split()
                data.append(temp)
            return data
    else:
        print('Справочник еще не создан')
        time.sleep(3)  # import time
        os.system("cls")
        return controller.show_menu()
