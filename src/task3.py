from task1 import pprint_message_tree, message_entropy, calculate_probability_of_symbol


def create_bin_message_tree(message: str) -> dict:
    message_tree = {}
    message = message.split(' ')

    for symbol in set(message):
        message_tree[symbol] = {'frequency': message.count(symbol)}

    for symbol in message_tree.keys():
        message_tree[symbol]['probability'] = calculate_probability_of_symbol(len(message),
                                                                              message_tree[symbol]['frequency'],
                                                                              symbol)

    message_tree['type'] = 'bin'

    return message_tree


def binary_encode(message: str) -> str:

    bin_message = []
    encoded_message = message.encode(encoding='ascii')

    print()
    print('-'*36)
    print('| Символ | Символ в двоичной форме  |')

    for i in range(len(message)):
        bin_num = str(bin(encoded_message[i])).replace('0b', '')
        bin_num = bin_num if len(bin_num) == 7 else '0' * (7 - len(bin_num)) + bin_num
        print(f'|    {message[i]}   |          {bin_num}         |')
        bin_message.append(bin_num)

    print('-' * 36)
    print()

    return " ".join(bin_message)


def get_redundancy(message_entropy: float, code_len: float = 7):
    return round(1 - message_entropy/code_len, 4)


def main(message, is_bin: bool = False):

    if not is_bin:
        message = binary_encode(message)
        print(f'Сообщение в двоичном коде: {message}')
        print('')

    bin_tree = create_bin_message_tree(message)
    print('')

    entropy = message_entropy(bin_tree)
    print('')

    pprint_message_tree(bin_tree)
    print('')

    r = get_redundancy(entropy)

    print(f"Энтропия сообщения: H(X) = ∑i(H(xi)) = {entropy} бит/символ")
    print(f"Длина кода в данном случае равна: L = 7 битам")
    print(f"Избыточность равна: R = 1 - H(X)/L = {entropy}/7 = {r}")

    return message


def run(message) -> str:
    print()
    print('-' * 10 + 'Задание №3' + '-' * 10)
    encoded_message = main(message)
    print()
    return encoded_message
