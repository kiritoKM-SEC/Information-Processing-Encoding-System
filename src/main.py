import task1, task2, task3, task4, task5, task6, task7 

from tools import get_num_values, clear_console


introduction = 'Программа создана для выполнения рассчетов по курсовой работе "Теория обработки информации"'
menu = """1) Рассчитать энтропию и избыточность источника с учетом cформированного 
сообщения по варианту
2) Рассчитать энтропию объединения двух ансамблей, если известно, что 
данные, сформированные источником, коррелируют с данными другого 
источника, вероятности совместного появления объединения заданы в таблице 
по варианту. Также найти условную энтропию при известных значениях 
второго источника, и рассчитать энтропию объединения, если данные будут 
независимы. 
3) Зашифровать данное сообщение с помощью шифра по варианту. 
4) Представить сообщение в бинарном коде и рассчитать энтропию и 
избыточность. 
5) Построить по варианту оптимальный код для сообщения, полученного после 
шифрования. Рассчитать энтропию и избыточность полученного после 
кодирования бинарного сообщения и сравнить с энтропией и избыточностью до 
кодирования. 
6) Провести физическое кодирование полученной в 5 п. последовательности с 
помощью кода по варианту. Определить минимальную ширину полосы частот 
полученного сигнала.
7) Найти пропускную способность дискретного канала связи и скорость 
передачи информации с учетом воздействия аддитивного гауссовского шума.
"""
print(introduction)
print(menu)

available_choices = '01234567'

answer = input('Выберите нужный номер задания или введите "0", чтобы выполнить все задания.\n>> ')

if len(answer) != 1 or answer not in available_choices:
    print('Такого задания нет!. Откройте программу заново')
    input()
    exit(0)

if answer == '0':
    # получаем все нужные исходные данные заданий
    message = input('Введите ваше сообщение\n>> ')
    file_name = input('Введите название файла\n>> ')

    probability_of_mistake = get_num_values(input('Введите вероятность ошибки\n>> '))

    time_of_packet = get_num_values(input('Введите время посылки\n>> '))

    # выполнение заданий
    task1.run(message)
    input('Для продолжения нажмите enter')
    clear_console()

    try:
        task2.run(file_name)
    except Exception as ex:
        print(f'Не удалось выполнить задание по причине: {ex}')
        input()
        exit(0)

    input('Для продолжения нажмите enter')
    clear_console()

    bin_message = task3.run(message)
    input('Для продолжения нажмите enter')
    clear_console()

    encoded_message = task4.run(bin_message)
    input('Для продолжения нажмите enter')
    clear_console()

    message_in_code = task5.run(encoded_message)
    input('Для продолжения нажмите enter')
    clear_console()

    task6.run(message_in_code, time_of_packet)
    input('Для продолжения нажмите enter')
    clear_console()

    task7.run(message_in_code, probability_of_mistake, time_of_packet)
    input('Для продолжения нажмите enter')
    clear_console()

else:
    match int(answer):
        case 1:
            message = input('Введите ваше сообщение\n>> ')
            task1.run(message)
        case 2:
            file_name = input('Введите название файла\n>> ')

            try:
                task2.run(file_name)
            except Exception as ex:
                print(f'Не удалось выполнить задание по причине: {ex}')
                input()
                exit(0)
        case 3:
            message = input('Введите ваше сообщение\n>> ')
            task3.run(message)
        case 4:
            bin_message = input('Введите ваше сообщение в двоичной форме\n>> ')
            task4.run(bin_message)
        case 5:
            encrypted_msg = input('Введите ваше зашифрованное сообщение в двоичной форме\n>> ')
            task5.run(encrypted_msg)
        case 6:
            time_of_packet = get_num_values(input('Введите время посылки\n>> '))
            message_in_codes = input('Введите ваше сообщение закодированное, оптимальным кодам')
            task6.run(message_in_codes, time_of_packet)
        case 7:
            message_in_codes = input('Введите ваше сообщение закодированное, оптимальным кодам')
            time_of_packet = get_num_values(input('Введите время посылки\n>> '))
            probability_of_mistake = get_num_values(input('Введите вероятность ошибки\n>> '))
            task7.run(message_in_codes, probability_of_mistake, time_of_packet)


print('Для завершения программы нажмите enter')
input()
