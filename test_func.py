import re
import sys
from itertools import count
from typing import List


def bracket_order():
    """
    """
    text = input('Введите скобочную последовательность: ')

    while '()' in text or '[]' in text or '{}' in text:
        text = text.replace('()', '')
        text = text.replace('[]', '')
        text = text.replace('{}', '')

    if len(text) == 0:
        print('yes')
    else:
        print('no')


def count_words_in_text() -> None:
    """
    Во входном файле записан текст. Словом считается
    последовательность непробельных символов идущих подряд, слова
    разделены одним или большим числом пробелов или символами конца строки.
    Определите, сколько различных слов содержится в этом тексте.
    """
    example_1 = (
        "She sells sea shells on the sea shore; "
        "The shells that she sells are sea shells I'm sure. "
        "So if she sells sea shells on the sea shore, "
        "I'm sure that the shells are sea shore shells."
    )
    example_2 = 'AA aa Aa aA'
    example_3 = 'a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a'
    answer = len(set(example_1.split(' ')))
    print(answer)


def synonym_dict() -> None:
    """
    Вам дан словарь, состоящий из пар слов.
    Каждое слово является синонимом к парному ему слову.
    Все слова в словаре различны.
    Для одного данного слова определите его синоним.

    Формат ввода
    Программа получает на вход количество пар синонимов N N.
    Далее следует N N строк, каждая строка содержит ровно два слова-синонима.
    После этого следует одно слово.

    Формат вывода
    Программа должна вывести синоним к данному слову.
    """
    syn_dict = {
        'Hello': 'Hi',
        'Bye': 'Goodbye',
        'List': 'Array',
    }
    word = 'Goodbye'
    word_syn = ''
    for key, value in syn_dict.items():
        if word == key:
            word_syn = value
        elif word == value:
            word_syn = key

    print(word_syn)


def min_in_length():
    """
    Рассмотрим последовательность целых чисел длины n n.
    По ней двигается «окно» длины k k: сначала в «окне» находятся первые k k чисел,
    на следующем шаге в «окне» уже будут находиться k k чисел, начиная со второго,
    и так далее до конца последовательности.
    Требуется для каждого положения «окна» определить минимум в нём.

    Формат ввода
    В первой строке входных данных содержатся два натуральных
    числа n и k (n ≤ 150000, k ≤ 10000, k ≤ n) —
    длины последовательности и «окна», соответственно.
    На следующей строке находятся n n целых чисел — сама последовательность.

    Формат вывода
    Выведите n − k + 1 строк.
    В каждой строке должно быть одно число — минимум для
    соответствующего положения «окна».
    """
    length = int(input(f'Введите количество цифр:'))
    step = int(input(f'Введите шаг:'))

    while True:
        nums = input(f'Введите {length} цифр:')
        nums_array = [int(num) for num in nums.split(' ')]
        if len(nums_array) == length:
            break

        print(f'Нужно ввести {length} цифр')

    for num in range(len(nums_array)):
        if num + step - 1 < len(nums_array):
            step_list = [nums_array[i] for i in range(num, num + step)]
            print(f'Min num: {min(step_list)}')


def good_string():
    """
    Первая строка ввода содержит единственное
    целое число N — количество различных букв в наборе.
    Обратите внимание: в наборе всегда используются N первых букв латинского алфавита.
    Следующие N строк содержат целые положительные числа c i — количество букв
    соответствующего типа. Таким образом, первое число означает количество букв "a",
    второе число задаёт количество букв "b" и так далее.

    Формат вывода
    Выведите единственное целое число — максимально возможную хорошесть строки,
    которую можно собрать из имеющихся дощечек.

    Примечание
    В первом тесте имеется по одной дощечке с каждой из 3 различных букв. Ответ 2 достигается на строке "abc"
    """
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    ]
    max_letters = int(input(f'Введите количество букв: '))
    list_input = ''

    for let in range(max_letters):
        int(input(f'Введите количество {let + 1} буквы: '))
        list_input += alphabet[let]

    print(f'Максимальная хорошесть строки: {len(set(list_input)) - 1}')


def not_three_one_in_a_row():
    """
    По данному числу N N определите количество последовательностей
    из нулей и единиц длины N N, в которых никакие три единицы не стоят рядом.

    Формат ввода
    Во входном файле написано натуральное число N N, не превосходящее 35

    Формат вывода
    Выведите количество искомых последовательностей.
    Гарантируется, что ответ не превосходит 2 ** 31 − 1
    """
    length = int(input('Введите длину цифр: '))

    a = [2, 4, 7]

    for i in range(3, 36):
        a.append(a[i - 1] + a[i - 2] + a[i - 3] % 12345)

    print(a[length - 1])


def letters_change():
    """
    Красотой строки назовем максимальное число идущих подряд одинаковых букв.
    (красота строки abcaabdddettq равна 3)
    Сделайте данную вам строку как можно более красивой,
    если вы можете сделать не более k операций замены символа.

    Формат ввода
    В первой строке записано одно целое число k
    Во второй строке дана непустая строчка S
    Строчка S состоит только из маленьких латинских букв.

    Формат вывода
    Выведите одно число — максимально возможную красоту строчки,
    которую можно получить.
    """
    change = int(input('Введите количество замен: '))
    string = input('Введите строку: ')

    num = change
    list_string = [i for i in string]

    max_nums_list = list()

    count = 1

    for let_1 in range(len(list_string)):
        if let_1 + 1 < len(list_string):

            for let_2 in range(let_1 + 1, len(list_string)):
                print(let_1, list_string[let_1])
                print(let_2, list_string[let_2])
                if list_string[let_1] == list_string[let_2]:
                    count += 1
                else:
                    if change > 0:
                        change -= 1
                        count += 1
                    else:
                        break

                if let_2 == len(list_string) - 1:
                    count += change
                    break

        max_nums_list.append(count)
        change = num
        count = 1

    print(f'Максимально возможная красота строки: {max(max_nums_list)}')


def histogram():
    """
    В первой строке входного файла записано число N — количество
    прямоугольников гистограммы. Далее в той же строке
    записано N целых чисел h. Эти числа обозначают высоты
    прямоугольников гистограммы слева направо.
    Ширина каждого прямоугольника равна 1

    Формат вывода
    Выведите площадь самого большого прямоугольника в гистограмме.
    Помните, что этот прямоугольник должен быть на общей базовой линии.
    """
    data = input('Введите количество прямоугольников и их длину: ').split(' ')

    elem_list = [int(num) for num in data if num != ' ']
    histograms_count = elem_list.pop(0)

    max_common_area = 0

    for elem in range(len(elem_list)):
        if elem + 1 < len(elem_list):
            common_length = min(elem_list[elem], elem_list[elem + 1])
            area = common_length * 2

            if area > max_common_area:
                max_common_area = area

    print(f'Площадь самого большого прямоугольника в гистограмме: {max_common_area}')


def max_multiplication_numbers():
    """
    Дан список, заполненный произвольными целыми числами.
    Найдите в этом списке два числа, произведение которых максимально.

    Формат ввода
    В единственной строке через пробел вводятся целые числа — элементы списка.
    Список содержит не менее двух и не более 100 000 чисел.
    Сами элементы по модулю не превышают 1 000 000.

    Формат вывода
    Выведите эти два числа в порядке неубывания

    Примечание
    Решение должно иметь сложность O(n), где n — размер списка.
    Гарантируется, что во всех тестах ответ однозначен.
    """
    num_string = input('Введите числа: ').split(' ')

    array = [int(num) for num in num_string if num != ' ']

    max_multy = 0

    for num_1 in range(len(array)):
        if num_1 + 1 < len(array):
            for num_2 in range(num_1 + 1, len(array)):
                multy = array[num_1] * array[num_2]
                if multy > max_multy:
                    max_multy = multy
                    answer = [array[num_1], array[num_2]]

    if answer[0] > answer[1]:
        print(answer[1], answer[0])
    else:
        print(answer[0], answer[1])


def add_more_candies():
    """
    У Карлсона дома есть набор из n n банок с конфетами.
    Банки пронумерованы от 1 до n, в i-й из них лежит a конфет.
    Карлсон считает набор банок симпатичным,
    если в этом наборе нет трех банок с разным числом конфет.

    У Карлсона есть неограниченный запас конфет в карманах,
    поэтому он может добавить в любую банку произвольное число конфет.
    Помогите ему определить, какое минимальное общее число конфет
    ему придется добавить, чтобы набор банок с конфетами стал симпатичным.

    Формат ввода
    Первая строка входных данных содержит натуральное
    число n — количество банок в наборе Карлсона.

    Вторая строка входных данных содержит n целых
    чисел a — число конфет в банках.
    Соседние числа отделены друг от друга одним пробелом.

    Формат вывода
    Выведите одно число — минимальное общее количество конфет,
    которое придется добавить, чтобы Карлсон считал набор банок симпатичным.

    Примечание
    В первом тесте из примера Карлсон может добавить в
    первую банку две конфеты, а во вторую банку — одну конфету.

    Тогда в первой и четвертой банках будет лежать по 7 конфет,
    а во второй и третьей — по 2 конфеты.

    Во втором тесте из примера набор банок исходно является симпатичным,
    добавлять конфеты не требуется
    """
    # pots = int(input('Введите количество банок: '))
    pots = 6
    candy_pots = '1 2 3'.split(' ')
    set_pots = set([int(num) for num in candy_pots])

    if len(set_pots) <= 2:
        print('Добавлять конфеты не требуется: 0')
        return

    candy_pots = list(set_pots)
    print(len(candy_pots))

    for i in range(len(candy_pots)):
        if i + 1 < len(candy_pots):
            for j in range(i + 1, len(candy_pots)):
                if candy_pots[i] > candy_pots[j]:
                    candy_pots[i], candy_pots[j] = candy_pots[j], candy_pots[i]

    print(candy_pots)
    mid = len(candy_pots) // 2

    middle_num = candy_pots[mid]

    print(middle_num)
    candy_pots.pop(mid)

    left_part = candy_pots[:mid]
    right_part = candy_pots[mid:]

    summ_left = sum_num(middle_num, left_part)
    summ_right = sum_num(middle_num, right_part)

    if summ_left > summ_right:
        right_part.append(middle_num)
    else:
        left_part.append(middle_num)

    print(left_part)
    print(right_part)

    left_candies = need_candies_at_one_side(left_part)
    right_candies = need_candies_at_one_side(right_part)

    total_min = left_candies + right_candies

    print(f'Всего: {total_min}')


def need_candies_at_one_side(array: List[int]):
    max_num = max(array)
    summary_left = 0

    for num in range(len(array)):
        summary_left += max_num - array[num]

    print(summary_left)
    return summary_left


def sum_num(num: int, array: List[int]):
    summ = 0

    for elem in range(len(array)):
        summ += abs(num - array[elem])
    print(summ)
    return summ


if __name__ == '__main__':
    # bracket_order()
    # count_words_in_text()
    # synonym_dict()
    # min_in_length()
    # good_string()
    # not_three_one_in_a_row()
    # letters_change()
    # histogram()
    # max_multiplication_numbers()
    add_more_candies()
