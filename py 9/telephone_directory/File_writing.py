
from os.path import exists
#path = 'Phonebook.csv'


def input_data(file):
    valid = exists(file)
    if not valid:
        creating_csv(file)


def creating_csv(file):
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'Фамилия;Имя;Телефон;Примечание\n')


def writing_scv(file, info):
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')
    return print("\nЗапись сохранена")


def writing_txt(file, info):
    file = f'{file}.txt'
    f = open(file, 'w')
    f.close()
    info.pop(0)
    for i in info:
        with open(file, 'a', encoding='utf-8') as data:
            data.write(
                f'Фамилия: {i[0]}\nИмя: {i[1]}\nТелефон: {i[2]}\nПримечание: {i[3]}\n\n')
    return print(f'Файл {file} создан.')


# def write_json(employees: list):
#     with open(Path.cwd() / 'database02.json', 'w', encoding='utf-8') as fout:
#         for employee in employees:
#             fout.write(json.dumps(employee) + '\n')
