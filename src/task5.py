import heapq
from math import ceil


from task1 import message_entropy
from task3 import get_redundancy, create_bin_message_tree


class HuffmanNode:
    def __init__(self, symbol=None, freq=0, left=None, right=None, code=None):
        self.symbol = symbol
        self.code = code
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(message_tree: dict) -> HuffmanNode:
    heap = []

    for symbol, data in message_tree.items():
        if symbol == 'type':
            continue
        # задаем очередь, которая автоматически сортируется
        # (по ленивому возрастанию, гарантировано, что в начале будет самый маленький элемент)
        # при добавлении нового элемента
        heapq.heappush(heap, HuffmanNode(symbol, data['frequency']))

    while len(heap) > 1:
        # выбираем 2 узла с минимальной частотой
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # создаём новый узел с суммой вероятности двух символов
        # не задаем символ, т.к. новый узел содержит только сумму первоначальных символов
        new_node = HuffmanNode(
            symbol=None,
            freq=left.freq + right.freq,
            left=left,
            right=right
        )

        heapq.heappush(heap, new_node)

    # корень дерева, то есть корень с вероятностью 1
    return heap[0]


def get_huffman_codes(root: HuffmanNode) -> dict:
    codes = {}

    def traverse(node, current_code):
        if node is None:
            return

        # если это символ(конец дерева) — сохраняем код и дальше уже не идем
        if node.symbol is not None:
            codes[node.symbol] = current_code
            return

        # идём влево — 0
        traverse(node.left, current_code + "0")
        # идём вправо — 1
        traverse(node.right, current_code + "1")

    traverse(root, "")

    return codes


def create_huffman_codes(message_tree: dict) -> dict:
    tree_root = build_huffman_tree(message_tree)
    return get_huffman_codes(tree_root)


def pprint_huffman_tree(codes: dict):

    print('-'* 32)
    print('| Двоичный код | Коды Хаффмана ')

    for bits in codes.keys():
        print('|' + ' ' * 4 + bits + ' ' * 3 + '|', end='')
        print(' ' * 7 + codes[bits], end='')
        print()

    print('-' * 32)


def get_message_in_codes(message: str, codes: dict) -> str:
    return ' '.join([str(codes[symbol]) for symbol in message.split()])


def get_average_code_len(bin_tree: dict):

    length = 0
    for bits in bin_tree.keys():

        if bits != 'type':
            length += len(bits) * bin_tree[bits]['probability']

    return round(length, 4)


def main(bin_message) -> str:
    print(bin_message)
    bin_tree = create_bin_message_tree(bin_message)
    codes = create_huffman_codes(bin_tree)
    (pprint_huffman_tree(codes))

    message_in_code = get_message_in_codes(bin_message, codes)
    codes_tree = create_bin_message_tree(message_in_code)
    print(f'Сообщения закодированной оптимальным кодом: {message_in_code}')

    entropy = message_entropy(codes_tree)
    print(f'Энтропия сообщения закодированного оптимальным кодом Хаффманна: H={entropy} бит/символ')
    length = get_average_code_len(codes_tree)
    print(f'Средняя длина сообщения равна: l = {length} бит')
    length = ceil(length)
    print(f'Округленная длина вверх до целых: L = {length}')
    redundancy = get_redundancy(entropy, length)
    print(f'Избыточность такого сообщения равна: R = {redundancy}')

    return message_in_code


def run(bin_message) -> str:
    print()
    print('-' * 10 + 'Задание №5' + '-' * 10)
    codes = main(bin_message)
    print()
    return codes












