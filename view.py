def show_menu():
    print('1 - показать все')
    print('2 - добавить запись')
    print('3 - удалить запись')
    print('4 - изменить телефон')
    print('5 - изменить должность')
    print('6 - изменить статус')
    print('7 - импортировать базу в txt-файл')
    return int(input('Введите цифру: '))

def delete():
    print('Введите ID для удаления')
    return int(input())

def change_tel():
    print('Введите ID для изменения')
    print('Введите новый телефон')
    return int(input()), input()

def change_position():
    print('Введите ID для изменения')
    print('Введите новую должность')
    return int(input()), input()

def change_status():
    print('Введите ID для изменения')
    print('Введите новый статус')
    return int(input()), input()

def show_res(res):
    for i, row in enumerate(res):
        print(i, ' '.join(row))

def add_info():
    print('Введите ФИО, телефон, должность, статус через пробел')
    in_info = input().split()
    return in_info

def add_info_again():      # Повторный запрос на ввод
    print('Добавить новую информацию?')
    print('Введите 1 - нет или 2 - да')
    new_info = int(input())
    return new_info

def show_export_txt():
    print('Выполнен экспорт файла в txt формат')