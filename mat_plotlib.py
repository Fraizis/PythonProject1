# import matplotlib.pyplot as plt
from matplotlib import pyplot


def make_2d():
    # координаты
    x = range(7)
    y1 = [6, 1, 5, 4, 3, 3, 4]

    y2 = [5, 4, 5, 3, 4, 2, 5]

    # размер
    pyplot.figure(figsize=(9, 6))

    # заголовок
    pyplot.title('Заголовок', fontsize=20)

    # название осей
    pyplot.xlabel('Ось X', fontsize=15)
    pyplot.ylabel('Ось Y', fontsize=15)

    # деления на осях
    pyplot.xticks(range(7),
                  labels=['Раз', 'Два', 'Три', 'Четыре', 'Пять', 'Шесть', 'Семь'],
                  fontsize=12,
                  rotation=45)
    pyplot.yticks(range(1, 6))

    # границы осей
    # pyplot.xlim(0, 8)
    # pyplot.ylim(0, 8)

    # сетка
    pyplot.grid()

    # создание
    pyplot.plot(x, y1, color='purple')
    pyplot.plot(x, y2, color='lightgreen')

    # легенда
    pyplot.legend(title='Графики', labels=['Первый график', 'Второй график'])

    # отображение
    pyplot.show()


if __name__ == '__main__':
    make_2d()
