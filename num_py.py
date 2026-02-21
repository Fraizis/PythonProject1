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


def operations():
    a = numpy.array([1, 2, 3])
    b = numpy.array([4, 5, 6])

    # Сложение
    sum_array = a + b  # результат: [5, 7, 9]

    # Вычитание
    sub_array = a - b  # результат: [-3, -3, -3]

    # Умножение
    mul_array = a * b  # результат: [4, 10, 18]

    # Деление
    div_array = a / b  # результат: [0.25, 0.4, 0.5]

    # Возведение в степень
    power_array = a ** 2  # результат: [1, 4, 9]

    # Бродкастинг: прибавляем скаляр к массиву
    c = numpy.array([1, 2, 3])
    d = 2
    result = c + d  # результат: [3, 4, 5]


def ufunc_numpy():
    # Создаем массив
    a = numpy.array([1, 4, 9, 16])

    # Вычисляем квадратный корень
    sqrt_array = numpy.sqrt(a)  # результат: [1. 2. 3. 4.]

    # Экспоненциальная функция
    b = numpy.array([0, 1, 2])

    exp_array = numpy.exp(b)  # результат: [1.         2.71828183 7.3890561 ]

    # Пример 1
    # Создаем массив углов в радианах
    angles = numpy.array([0, numpy.pi / 2, numpy.pi])
    print(angles)
    # Вычисляем синус
    sin_array = numpy.sin(angles)  # результат: [0. 1. 0.]

    # Пример 2
    # Вычисляем синус
    numpy.sin(numpy.pi / 2.)  # результат: 1.0

    cos_array = numpy.cos(angles)  # результат: [1. 0.  -1.]

    tan_array = numpy.tan(angles)  # результат: [0.  -inf.  0.]

    # Создаем массив положительных значений
    c = numpy.array([1, numpy.e, numpy.e ** 2])

    log_array = numpy.log(c)  # результат: [0. 1. 2.]

    x = numpy.array([1, 2, 3])

    # Применяем несколько ufunc
    result = numpy.sqrt(numpy.exp(x))  # вычисляем √(e^x) для каждого элемента


def statistic_numpy():
    # Создаем массив
    data = numpy.array([1, 2, 3, 4, 5])

    # Вычисляем среднее
    mean_value = numpy.mean(data)  # результат: 3.0

    median_value = numpy.median(data)  # результат: 3.0

    std_value = numpy.std(data)  # результат: 1.4142135623730951

    var_value = numpy.var(data)  # результат: 2.0

    min_value = numpy.min(data)  # результат: 1
    max_value = numpy.max(data)  # результат: 5

    # 25-й и 75-й процентили
    q25 = numpy.percentile(data, 25)  # результат: 2.0
    q75 = numpy.percentile(data, 75)  # результат: 4.0

    # Создаем двумерный массив
    matrix = numpy.array([[1, 2, 3], [4, 5, 6]])

    # Среднее по строкам
    mean_rows = numpy.mean(matrix, axis=1)  # результат: [2. 5.]

    # Среднее по столбцам
    mean_columns = numpy.mean(matrix, axis=0)  # результат: [2.5 3.5 4.5]


def concatenate_arr():
    # Создаем два одномерных массива
    a = numpy.array([1, 2, 3])
    b = numpy.array([4, 5, 6])

    # Объединяем их
    result = numpy.concatenate((a, b))
    print(result)  # Output: [1 2 3 4 5 6]

    # Создаем два двумерных массива
    a = numpy.array([[1, 2, 3], [4, 5, 6]])
    b = numpy.array([[7, 8, 9]])

    # Объединяем вдоль первой оси (по строкам)
    result = numpy.concatenate((a, b), axis=0)
    print(result)
    # Output:
    # [[1 2 3]
    #  [4 5 6]
    #  [7 8 9]]

    # Создаем два двумерных массива
    a = numpy.array([[1, 2, 3], [4, 5, 6]])
    b = numpy.array([[7, 8, 9]])

    # Объединяем их по вертикали
    result = numpy.vstack((a, b))
    print(result)
    # Output:
    # [[1 2 3]
    #  [4 5 6]
    #  [7 8 9]]

    # Создаем два двумерных массива
    a = numpy.array([[1, 2, 3], [4, 5, 6]])
    b = numpy.array([[7], [8]])

    # Объединяем их по горизонтали
    result = numpy.hstack((a, b))
    print(result)
    # Output:
    # [[1 2 3 7]
    #  [4 5 6 8]]

    # Разделение массивов

    # Создаем одномерный массив
    a = numpy.array([1, 2, 3, 4, 5, 6])

    # Разделяем массив на 3 части
    result = numpy.split(a, 3)
    print(result)  # Output: [array([1, 2]), array([3, 4]), array([5, 6])]

    # Создаем двумерный массив
    a = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Разделяем массив на 3 части по первой оси (по строкам)
    result = numpy.split(a, 3, axis=0)
    print(result)
    # Output:
    # [array([[1, 2, 3]]), array([[4, 5, 6]]), array([[7, 8, 9]])]

    # Создаем двумерный массив
    a = numpy.array([[1, 2, 3], [4, 5, 6]])

    # Разделяем массив на 3 части по горизонтали
    result = numpy.hsplit(a, 3)
    print(result)
    # Output: [array([[1],
    #                 [4]]),
    #           array([[2],
    #                 [5]]),
    #           array([[3],
    #                 [6]])]

    # Создаем двумерный массив
    a = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Разделяем массив на 3 части по вертикали
    result = numpy.vsplit(a, 3)
    print(result)
    # Output:
    # [array([[1, 2, 3]]), array([[4, 5, 6]]), array([[7, 8, 9]])]


def mask_numpy():
    # Создаем массив
    a = numpy.array([10, 20, 30, 40, 50])

    # Создаем булевый массив, выделяя элементы больше 30
    mask = a > 30

    print(mask)  # Output: [False False False  True  True]

    # Используем булевый массив для извлечения элементов
    filtered = a[mask]
    print(filtered)  # Output: [40 50]

    # Создаем массив
    a = numpy.array([10, 20, 30, 40, 50])

    # Используем маскировку для извлечения элементов больше 30
    filtered = a[a > 30]
    print(filtered)  # Output: [40 50]

    # Создаем двумерный массив
    b = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Создаем маску для элементов больше 5
    mask = b > 5

    print(mask)
    # Output:
    # [[False False False]
    #  [False False  True]
    #  [ True  True  True]]

    # Используем маску для извлечения элементов
    filtered = b[mask]
    print(filtered)  # Output: [6 7 8 9]

    # Создаем массив
    # a = numpy.array([10, 20, 30, 40, 50])

    # Извлекаем элементы, которые больше 20 и меньше 50
    filtered = a[(a > 20) & (a < 50)]
    print(filtered)  # Output: [30 40]


if __name__ == '__main__':
    print()
    a = numpy.array([x for x in range(16)]).reshape(4, 4)
    # res = numpy.vsplit(a, 2)
    array_2d = numpy.array([[12, 25, 7, 45],
                         [30, 18, 50, 2],
                         [60, 75, 5, 20],
                         [15, 9, 33, 42]])
    array_2d[array_2d < 20] = 0
    print(array_2d)
