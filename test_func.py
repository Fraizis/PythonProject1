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
    n = 7
    k = 3
    # while True:
    #     nums = input(f'Введите {n} цифр:')
    #     nums_array = nums.split(' ')
    #     if len(nums_array) == n:
    #         break
    #
    #     print(f'Нужно ввести {n} цифр')

    array = '1 3 2 4 5 3 1'
    nums_array = [int(num) for num in array.split(' ')]

    for num in range(len(nums_array)):
        if num + k - 1 < len(nums_array):
            min_num_list = [nums_array[i] for i in range(num, num + k)]
            print(f'Min num: {min(min_num_list)}')


if __name__ == '__main__':
    # bracket_order()
    # count_words_in_text()
    # synonym_dict()
    min_in_length()
