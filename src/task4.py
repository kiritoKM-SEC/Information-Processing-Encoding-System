from random import choice
from string import ascii_letters

from task3 import binary_encode
from task3 import main as task3


def generate_random_key(n: int) -> str:
    return ''.join([choice(ascii_letters) for _ in range(n)])


def xor(bit1: str, bit2: str) -> str:
    return str(int(bit1 != bit2))


def encrypt(bin_message: str, bin_key: str) -> str:

    encrypt_message = ''

    for i in range(len(bin_message)):

        if bin_message[i] != ' ':
            encrypt_message += xor(bin_message[i], bin_key[i])
        else:
            encrypt_message += ' '

    return encrypt_message

def binary_decode(bin_message: str):

    message = ''
    for symbol in bin_message.split(' '):
        message += symbol_from_bits(symbol)

    return message


def main(bin_message: str):
    key = generate_random_key(len(bin_message.split(' ')))
    print(f'Сгенирированный случайный ключ: {key}')
    bin_key = binary_encode(key)
    print(f'Ключ в двоичной форме: ' + str(bin_key))

    print(f'Исходное сообщение в двоичной форм: {bin_message}')
    encrypted_message = encrypt(bin_message, bin_key)

    print(f'Зашифрованное сообщение в двоичной форме: {encrypted_message}')

    task3(encrypted_message, is_bin=True) # рассчитаем энтропию после кодирования

    return encrypted_message


def run(bin_message) -> str:
    print()
    print('-' * 10 + 'Задание №4' + '-' * 10)
    encoded_message = main(bin_message)
    print()
    return encoded_message

