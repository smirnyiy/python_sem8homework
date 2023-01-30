import csv

def csv_data_open():      # 1 - показать все
    with open("csv_data.csv", encoding='utf-8') as file:
        file_csv = csv.reader(file, delimiter=";")
        res = list(file_csv)
    return res

def add_info(list):  # 2- добавление информации
    with open("csv_data.csv", "a", encoding="utf8", newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(list)

def del_info(index):  # удаление информации
    list_csv = csv_data_open()
    print(list_csv)
    del list_csv[index]
    with open("csv_data.csv", "w", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)


def update_info(index, tel):  # обновление информации
    list_csv = csv_data_open()
    list_csv[index][3] = tel
    with open("csv_data.csv", "w", encoding="utf8", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in list_csv:
            writer.writerow(row)

def import_into_csv():   # импорт из csv в txt формат
    with open("csv_data.csv", encoding='utf-8') as file:
        file_csv = csv.reader(file)
        res = list(file_csv)
    with open("txt_data.txt", 'w') as txt_file:
        for row in res:
            txt_file.writelines(row)
            txt_file.writelines('\n')