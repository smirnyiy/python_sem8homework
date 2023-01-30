import model
import view


def run():
    start = view.show_menu()
    if start == 1:
        res = model.csv_data_open()
        view.show_res(res)
    elif start == 2:
        add_again = 0   # Повторный запрос на ввод
        while add_again != 1:
            in_info = view.add_info()
            model.add_info(in_info)
            add_again = view.add_info_again()
    elif start == 3:
        view.show_res(model.csv_data_open()) 
        id = view.delete()
        model.del_info(id)
    elif start == 4:
        view.show_res(model.csv_data_open()) 
        id, tel = view.change_tel()
        model.update_info(id, tel)
    elif start == 5:
        view.show_res(model.csv_data_open()) 
        id, position = view.change_position()
        model.update_info(id, position)
    elif start == 6:
        view.show_res(model.csv_data_open()) 
        id, status = view.change_status()
        model.update_info(id, status)
    elif start == 7:    
        model.import_into_csv()
        view.show_export_txt()
    