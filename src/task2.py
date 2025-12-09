from math import log2


def convert_float_list_to_str(ls: list) -> list:
    copy_of_ls = ls.copy()
    str_ls = [str(num) for num in copy_of_ls]
    return str_ls


def create_matrix(file_name: str ='matrix.txt') -> list:
    matrix = []

    with open(file_name, 'r') as f:
        row = f.readline()

        while row:
            matrix.append([float(element.replace(',', '.')) for element in row.split(' ')])
            row = f.readline()
    return matrix


def pprint_matrix(matrix: list):

    print('|      |', end='')
    for i in range(len(matrix[0])):
        if i > 8:
            print(' ' * 2 + f'x{i + 1}' + ' ' * 2 + '|' , end='')
        else:
            print(' ' * 2 + f'x{i+1}' + ' ' * 3 + '|' , end='')

    print()

    for i in range(len(matrix)):

        print(f'|  y{i + 1}  |' , end='')
        for j in range(len(matrix[i])):

            element = str(matrix[i][j])

            if len(element) == 3:
                print(' ' * 2 + str(matrix[i][j]) + ' ' * 2 + '|' , end='')
            elif len(element) == 4:
                print(' ' + str(matrix[i][j]) + ' ' * 2 + '|' , end='')
            else:
                print(' ' + str(matrix[i][j]) + ' |' , end='')

        print()


def get_union_entropy(matrix: list) -> float:

    total_entropy = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            if matrix[i][j] == 0:
                entropy = 0
            else:
                entropy = (-1) * round(matrix[i][j] * log2(matrix[i][j]), 4)

            total_entropy += entropy
            print(f'H(x{j+1}, y{i+1}) = P(x{j+1}, y{i+1})log2P(x{j+1}, y{i+1}) = -{matrix[i][j]}log2({matrix[i][j]})) = {entropy} бит')

    print(f'Энтропия объединения равна H(x, y) = ∑i∑j(H(xj, yi)) = {total_entropy} бит')
    return total_entropy


def get_margin_y_probability(matrix: list) -> list:
    margin_probabilities = []

    print("Вычисление маргинальной вероятности по Y")

    for i in range(len(matrix)):
        margin_probability = round(sum(matrix[i]), 4)
        margin_probabilities.append(margin_probability)
        print(f'P(Y{i+1}) = ∑i(p(xi, y{i+1})) = {" + ".join(convert_float_list_to_str(matrix[i]))} = {margin_probability}')

    return margin_probabilities


def get_margin_x_probability(matrix: list) -> list:
    margin_probabilities = []

    print("Вычисление маргинальной вероятности по X")

    for i in range(len(matrix[0])):
        margin_probability = [matrix[j][i] for j in range(len(matrix))]
        sum_margin_probability = round(sum(margin_probability), 4)
        margin_probabilities.append(sum_margin_probability)
        print(f'P(X{i+1}) = ∑i(p(x{i+1}, yi)) = {" + ".join(convert_float_list_to_str(margin_probability))} = {sum_margin_probability}')

    return margin_probabilities


def get_conditional_entropy(matrix: list):
    margin_probabilities = get_margin_y_probability(matrix)
    total_conditional_entropy = 0

    for i in range(len(matrix)):

        y_entropy = 0
        print(f'Условная энтропия для P(Y{i+1})={margin_probabilities[i]}:')
        for j in range(len(matrix[i])):

            if matrix[i][j] == 0:
                conditional_entropy = 0
                conditional_probability = 0
            else:
                conditional_probability: float = round(matrix[i][j] / margin_probabilities[i], 4)
                conditional_entropy = round((-1) * conditional_probability * log2(conditional_probability), 4)

            print(f'P(x{j+1}/y{i+1}) = P(x{j+1}, y{i+1})/P(Y{i+1}) = {matrix[i][j]}/{margin_probabilities[i]} = {conditional_probability}')
            print(f'H(x{j+1}/y{i+1}) = -P(x{j+1}/y{i+1})log2(P(x{j+1}/y{i+1})) = {conditional_entropy}log2({conditional_entropy}) = {conditional_entropy} бит')
            print()

            y_entropy += conditional_entropy

        inner_contribution = round(y_entropy * margin_probabilities[i], 4)

        print('\n' + '-' * 85)
        print(f'Условная энтропия для y = {i+1}: H(X|Y=y{i+1}) = -∑i∑j(H(xj/yi) = {y_entropy} бит')
        print(f'Вклад Условной энтропия для y = {i + 1}:'
              f' P(Y{i+1}) * H(X|Y=y{i + 1}) = {margin_probabilities[i]} * {y_entropy} = {inner_contribution} бит')
        print('-' * 85 + '\n')
        total_conditional_entropy += inner_contribution

    print()
    print(f'Условная энтропия: H(X|Y) = ∑i(P(Yi) * H(X|Y=yi)) = {total_conditional_entropy} бит')


def get_margin_entropy(probabilities: list, symbol: str) -> float:
    total_entropy = 0

    print(f'Маргинальная энтропия по {symbol}: H({symbol}) = -∑i(P({symbol}i)*log2(P({symbol}i)) =' , end=' ')

    for i in range(len(probabilities)):
        entropy = (-1) * probabilities[i] * log2(probabilities[i])
        print(f'{probabilities[i]} * log2({probabilities[i]})' , end='')

        if i < len(probabilities) - 1:
            print(' + ', end='')

        total_entropy += entropy

    total_entropy = round(total_entropy, 4)

    print(f'= {total_entropy} бит')

    return total_entropy


def get_independent_union_entropy(matrix):
    margin_x_probabilities = get_margin_x_probability(matrix)
    margin_y_probabilities = get_margin_y_probability(matrix)

    entropy_x = get_margin_entropy(margin_x_probabilities, 'X')
    entropy_y = get_margin_entropy(margin_y_probabilities, 'Y')
    independent_union_entropy = round(entropy_x + entropy_y, 4)

    print(f'Энтропия объединения независимых данных:'
          f' H(X, Y) = H(X) + H(Y) = {entropy_x} + {entropy_y} = {independent_union_entropy} бит')


def main(file_name: str):
    matrix = create_matrix(file_name)

    answer = input('Чтобы отобразить табицу введите "+".\nЧтобы продолжить нажмите enter\n>> ')

    if answer == '+':
        pprint_matrix(matrix)

    print()
    print('Вычисление энтропии объединения')
    get_union_entropy(matrix)
    print()

    print()
    print('Вычисление условной энтропии')
    get_conditional_entropy(matrix)
    print()

    print()
    print('Вычисление энтропии объединения независимых данных')
    get_independent_union_entropy(matrix)


def run(file_name):
    print()
    print('-' * 10 + 'Задание №2' + '-' * 10)
    main(file_name)
    print()
