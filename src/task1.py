from math import log2


def create_str_message_tree(message: str) -> dict:
    message_tree = {}

    for symbol in set(message):
        message_tree[symbol] = {'frequency': message.count(symbol)}

    for symbol in message_tree.keys():
        message_tree[symbol]['probability'] = calculate_probability_of_symbol(len(message),
                                                                              message_tree[symbol]['frequency'], symbol)

    message_tree['type'] = 'str'

    return message_tree


def calculate_probability_of_symbol(message_len: int, symbol_frequency: int, symbol: str) -> float:
    probability = round(symbol_frequency / message_len, 4)
    print(f'P({symbol}) = n/N = {symbol_frequency}/{message_len}={probability}')
    return probability


def pprint_message_tree(message_tree: dict):
    print('-' * 46)
    print('| Символ | Частота | Вероятность | Энтропия  |')

    for uniq_symbol in message_tree.keys():

        if uniq_symbol == 'type':
            continue

        if message_tree.get('type') == 'bin':
            print(f'|{uniq_symbol} |   {message_tree[uniq_symbol]["frequency"]}     '
                  f'|   {message_tree[uniq_symbol]["probability"]}    |   {message_tree[uniq_symbol]["entropy"]}  |')
        else:
            print(f'|   {uniq_symbol}    |   {message_tree[uniq_symbol]["frequency"]}     '
              f'|   {message_tree[uniq_symbol]["probability"]}    |   {message_tree[uniq_symbol]["entropy"]}  |')

    print('-' * 45)


def message_entropy(message_tree: dict):

    message_len = sum([freq['frequency'] for freq in message_tree.values() if freq is dict])
    total_entropy = 0

    for uniq_symbol in message_tree.keys():

        if uniq_symbol == 'type':
            continue

        probability = message_tree[uniq_symbol]['probability']
        symbol_entropy = round(probability * log2(probability), 4) * -1

        print(f'H({uniq_symbol}) = P({uniq_symbol}) * log2(P({uniq_symbol})) = {probability} * log2({probability}) = {symbol_entropy} бит')

        message_tree[uniq_symbol]['entropy'] = symbol_entropy

        total_entropy += symbol_entropy

    return round(total_entropy, 4)


def max_entropy(len_uniq_symbol: int) -> float:
    return round(log2(len_uniq_symbol), 4)


def redundancy(m_entropy: float, message_entropy:float):
    return round(1 - message_entropy/m_entropy, 4)


def count_unique_symbol(message: str) -> int:
    return len(set(message))


def main(message) -> str:
    str_tree = create_str_message_tree(message)
    print('')

    entropy = message_entropy(str_tree)
    print('')

    pprint_message_tree(str_tree)
    print('')

    m_entropy = max_entropy(count_unique_symbol(message))
    r = redundancy(m_entropy, entropy)

    print(f"Энтропия сообщения: H(x) = ∑i(H(xi)) = {entropy} бит/символ")
    print(f"Максимальная энтропия:  Hmax = log2N = log{count_unique_symbol(message)}  = {m_entropy} бит/символ")
    print(f"Избыточность равна: R = 1 - H(X)/Hmax = 1 - {entropy}/{m_entropy} = {r}")

    return message


def run(message):
    print()
    print('-' * 10 + 'Задание №1' + '-' * 10)
    main(message)
    print()

