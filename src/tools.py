import os


def check_is_digit(num: str) -> bool:
    return num.replace(',', '').replace('.', '').isdigit()


def convert_str_to_float(num: str) -> float:
    return float(num.replace(',', '.'))


def get_num_values(num) -> float:

    if not check_is_digit(num):
        print('Введите числовое значение! Перезапустите программу')
        exit(0)

    return convert_str_to_float(num)


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

