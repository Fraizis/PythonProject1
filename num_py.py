import numpy


def create_arr():
    # Создание одномерного массива из списка
    array_1d = numpy.array([1, 2, 3, 4, 5])
    print("Одномерный массив:", array_1d)

    # Создание двумерного массива (матрицы) из списка списков
    array_2d = numpy.array([[1, 2, 3], [4, 5, 6]])
    print("Двумерный массив:\n", array_2d)

    # Создание массива с указанием типа данных
    array_float = numpy.array([1, 2, 3], dtype=float)
    print("Массив с типом float:", array_float)

    # Создание массива из кортежа
    tuple_data = (7, 8, 9)
    array_from_tuple = numpy.array(tuple_data)
    print("Массив из кортежа:", array_from_tuple)

    # Создание одномерного массива из 5 нулей
    array_zeros_1d = numpy.zeros(5)
    print("Одномерный массив нулей:", array_zeros_1d)

    # Создание двумерного массива 2x3, заполненного нулями
    array_zeros_2d = numpy.zeros((2, 3))
    print("Двумерный массив нулей:\n", array_zeros_2d)

    # Создание одномерного массива из 4 единиц
    array_ones_1d = numpy.ones(4)
    print("Одномерный массив единиц:", array_ones_1d)

    # Создание двумерного массива 3x2, заполненного единицами
    array_ones_2d = numpy.ones((3, 2))
    print("Двумерный массив единиц:\n", array_ones_2d)

    # Получаем первое и второе элементы из второй и третьей строк
    print(array_ones_2d[1:3, 0:2])  # Вывод: [[4 5]
    #          [7 8]]

    # Создание массива от 0 до 9
    array_range_1 = numpy.arange(10)
    print("Массив от 0 до 9:", array_range_1)

    # Создание массива от 1 до 10 с шагом 2
    array_range_2 = numpy.arange(1, 10, 2)
    print("Массив от 1 до 9 с шагом 2:", array_range_2)

    # Создание массива из 5 равноотстоящих значений от 0 до 1
    array_linspace_1 = numpy.linspace(0, 1, num=5)
    print("Массив из 5 равноотстоящих значений от 0 до 1:", array_linspace_1)

    # Создание массива из 4 равноотстоящих значений от 10 до 20, включая 20
    array_linspace_2 = numpy.linspace(10, 20, num=4, endpoint=True)
    print("Массив из 4 равноотстоящих значений от 10 до 20:", array_linspace_2)

    # Создание массива из 5 равноотстоящих значений от 0 до 1 с возвратом шага
    array_linspace_3, step = numpy.linspace(0, 1, num=5, retstep=True)
    print("Массив из 5 равноотстоящих значений от 0 до 1 с шагом:", array_linspace_3)
    print("Шаг между значениями:", step)

    # вычисляет среднее значение элементов массива.
    avg_arr = numpy.mean(array_linspace_2)
    print("Среднее значение элементов массива:", avg_arr)

    array_zeros = numpy.zeros((4, 3))
    print(array_zeros)

    array_d = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(array_d)

    # Получаем первое и второе элементы из второй и третьей строк
    print(array_2d[1:3, 0:2])  # Вывод: [[4 5]
    #          [7 8]]


def ndim_shape_prop():
    # Создаем 1D массив
    array_1d = numpy.array([1, 2, 3])
    print(array_1d.ndim)  # Вывод: 1

    # Создаем 2D массив
    array_2d = numpy.array([[1, 2], [3, 4]])
    print(array_2d.ndim)  # Вывод: 2

    # Создаем 3D массив
    array_3d = numpy.array([[[1], [2]], [[3], [4]]])
    print(array_3d.ndim)  # Вывод: 3

    # Размеры 2D массива
    print(array_2d.shape)  # Вывод: (2, 2) - 2 строки и 2 столбца

    # Размеры 3D массива
    print(array_3d.shape)  # Вывод: (2, 2, 1) - 2 "плоскости", 2 строки и 1 столбец


def dtype_prop():
    int_array = numpy.array([1, 2, 3])
    print(int_array.dtype)  # Вывод: int64 (или другой тип в зависимости от платформы)

    # Создаем массив с плавающей точкой
    float_array = numpy.array([1.0, 2.0, 3.0])
    print(float_array.dtype)  # Вывод: float64

    # Создаем массив со строками
    str_array = numpy.array(['a', 'b', 'c'])
    print(str_array.dtype)  # Вывод: <U1 (Unicode)

    # Получаем первый элемент
    print(float_array[0])  # Вывод: 10

    # Получаем третий элемент
    print(float_array[2])  # Вывод: 30

    # Изменяем третий элемент (индекс 2) на 100
    int_array[2] = 100
    print(int_array)  # Вывод: [1  2 100]

def reshape_change_arr():
    # Создаем одномерный массив
    array_1d = numpy.array([1, 2, 3, 4, 5, 6])

    # Изменяем форму на 2 строки и 3 столбца
    array_2d = array_1d.reshape(2, 3)
    print(array_2d)
    # Вывод:
    # [[1 2 3]
    #  [4 5 6]]

    # Создаем 3D массив
    array_3d = numpy.arange(27).reshape(3, 3, 3)
    print(array_3d)
    # Вывод:
    # [[[ 0  1  2]
    #   [ 3  4  5]
    #   [ 6  7  8]]
    #
    #  [[ 9 10 11]
    #   [12 13 14]
    #   [15 16 17]]
    #
    #  [[18 19 20]
    #   [21 22 23]
    #   [24 25 26]]]

    # Изменяем форму массива, позволяя NumPy вычислить одно из измерений
    array = numpy.arange(12).reshape(3, -1)
    print(array)
    # Вывод:
    # [[ 0  1  2  3]
    #  [ 4  5  6  7]
    #  [ 8  9 10 11]]

def odd_arr_index():
    array_1d = numpy.array([n for n in range(10)])
    print(array_1d)
    even_indices = numpy.where(array_1d % 2 == 0)

    print(f"Индексы чётных элементов: {even_indices[0]}")


def arr_2d():
    a = numpy.arange(1, 17).reshape(4, 4)
    elem = a[1][2]
    print(a)
    print(elem)

def change_rows():
    arr = numpy.arange(1, 10).reshape(3, 3)
    arr[:, [0, 2]] = arr[:, [2, 0]]
    print(arr)



if __name__ == '__main__':
    print()
    change_rows()
