from math import log2

from task1 import calculate_probability_of_symbol


def get_symbols_probability(message_in_codes: str) -> dict:
    message_in_codes = message_in_codes.replace(' ', '')
    length = len(message_in_codes)

    symbols_probability = {
        '0': calculate_probability_of_symbol(length, message_in_codes.count('0'), '0'),
        '1': calculate_probability_of_symbol(length , message_in_codes.count('1') , '1') ,
    }

    return symbols_probability


def get_flow_capacity(time_of_packet: float, probability_of_mistake: float) -> float:
    capacity = (1/time_of_packet) * ( 1 + probability_of_mistake*log2(probability_of_mistake)
                                       + (1 - probability_of_mistake) * log2(1-probability_of_mistake) )
    return round(capacity, 4)


def get_real_speed(symbols_probability: dict, probability_of_mistake: float, time_of_packet: float):
    real_speed = (1/time_of_packet) * \
                 ( (-1)*sum([probability*log2(probability) for probability in symbols_probability.values()])
                  +  probability_of_mistake*log2(probability_of_mistake)
                  + (1 - probability_of_mistake) * log2(1-probability_of_mistake))
    return round(real_speed, 4)


def main(message_in_code: str, probability_of_mistake: float, time_of_packet: float):
    flow_capacity = get_flow_capacity(time_of_packet , probability_of_mistake)
    print('Пропускная способность канала:\n'
          f'C = 1/t*(1 + P*log2(P) + (1-P)*log2(1-P)) = '
          f'1/{time_of_packet}*(1 + {probability_of_mistake}*log2({probability_of_mistake})'
          f' + (1-{probability_of_mistake})log2(1-{probability_of_mistake})) = {flow_capacity} бит/c')

    symbols_probability = get_symbols_probability(message_in_code)

    real_speed = get_real_speed(symbols_probability, probability_of_mistake, time_of_packet)
    print(f'Скорость передачи информации: R = 1/t*(-sum(Pi*log2(Pi)) + P*log2(P) + (1-P)*log2(1-P)) = \n'
          f' = 1/{time_of_packet}*'
          f'( -({" + ".join([f"{prob} * log2({prob})" for prob in symbols_probability.values()])}) + {probability_of_mistake}*log2({probability_of_mistake})'
          f' + (1-{probability_of_mistake})log2(1-{probability_of_mistake})) = '
          f'{real_speed} бит/c')


def run(message_in_code: str, probability_of_mistake, time_of_packet: float):
    print()
    print('-' * 10 + 'Задание №7' + '-' * 10)
    main(message_in_code, probability_of_mistake, time_of_packet)
    print()
