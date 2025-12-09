import matplotlib.pyplot as plt


class Graphic:

    def __init__(self, bin_message, time_of_packet):
        self.bin_message = bin_message
        self.time_of_packet = time_of_packet

    def add_text_to_bits_pair(self, code: str, start_coord_x: float):
        end_coord_x = start_coord_x + self.time_of_packet * len(code)
        text_position_x = (end_coord_x + start_coord_x) / 2

        plt.plot([start_coord_x, start_coord_x], [1.02, -0.05], '--ok')
        plt.plot([start_coord_x, end_coord_x] , [1.02, 1.02], '--ok')

        plt.text(text_position_x, 1.03, code, fontsize=10)

    def write_bit(self, bit: str, start_coord_x: float):
        end_coord_x = start_coord_x + self.time_of_packet
        text_position_x = (end_coord_x + start_coord_x) / 2
        plt.text(text_position_x, -0.08, bit, fontsize=10)

    def draw_rz(self):
        pairs_of_bin = self.bin_message.split()
        plt.figure()

        last_coord_X = 0

        for i in range(len(pairs_of_bin)):
            last_coord_X = self.draw_pair_of_bit(pairs_of_bin[i] , last_coord_X)

        plt.title("Физическое кодирование RZ")
        plt.xlabel('t, с' , fontsize=20)
        plt.ylabel('U, В' , fontsize=20)
        plt.show()

    def draw_pair_of_bit(self, pair: str, last_x_cord: int) -> float:

        self.add_text_to_bits_pair(pair, last_x_cord)
        colors = ['r-' , 'b-']

        for i in range(len(pair)):
            bit_color = colors[i % 2 == 0]

            self.write_bit(pair[i], last_x_cord)

            # рисуем бит 1
            if pair[i] == '1':

                coordinate_x = [last_x_cord, last_x_cord,
                                     last_x_cord,
                                     last_x_cord + self.time_of_packet/2,
                                     last_x_cord + self.time_of_packet/2,
                                     last_x_cord + self.time_of_packet]
                last_x_cord += self.time_of_packet
                coordinate_y = [0, 1, 1, 1, 0, 0]

            else:
                coordinate_x = [last_x_cord, last_x_cord + self.time_of_packet]
                last_x_cord += self.time_of_packet
                coordinate_y = [0, 0]


            plt.plot(coordinate_x, coordinate_y, bit_color)

        return last_x_cord

    def show(self):
        self.draw_rz()


def get_spectral_width(time_of_packet):
    return round(2/time_of_packet, 4)


def main(message_in_code: str, time_of_packet: float):
    spectral_width = get_spectral_width(time_of_packet)
    print(f'Минимальная ширина спектра: Fmin = 2/(t) = 2/({time_of_packet}) = {spectral_width} Гц')

    # строим график
    choice = input("Для того, чтобы увидеть график введите '+'\n>>  ")

    if choice == '+':
        graphic = Graphic(message_in_code, time_of_packet)
        graphic.show()


def run(message_in_code: str, time_of_packet: float):
    print()
    print('-' * 10 + 'Задание №6' + '-' * 10)
    main(message_in_code, time_of_packet)
    print()