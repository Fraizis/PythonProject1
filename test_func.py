import re
import sys


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
    Во входном файле написано натуральное число N N, не превосходящее 35 35.

    Формат вывода
    Выведите количество искомых последовательностей.
    Гарантируется, что ответ не превосходит 2 ** 31 − 1
    """

    length = int(input('Введите длину цифр: '))

    a = [2, 4, 7]

    for i in range(3, 36):
        a.append(a[i - 1] + a[i - 2] + a[i - 3] % 12345)
    print(a[length - 1])



def add_more_candies():
    # pots = int(input('Введите количество банок: '))
    pots = 4


if __name__ == '__main__':
    # bracket_order()
    # count_words_in_text()
    # synonym_dict()
    # min_in_length()
    # good_string()
    not_three_one_in_a_row()
