import os
import time
from collections import deque
from os import listdir
from os.path import isfile, join
from typing import List, Optional


def bracket_order() -> str:
    text = input('Введите скобочную последовательность: ')

    while '()' in text or '[]' in text or '{}' in text:
        text = text.replace('()', '')
        text = text.replace('[]', '')
        text = text.replace('{}', '')

    if len(text) == 0:
        return 'yes'
    else:
        return 'no'


def count_words_in_text() -> int:
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
    return answer


def synonym_dict() -> str:
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

    return word_syn


def min_in_length():
    """
    Рассмотрим последовательность целых чисел длины n n.
    По ней двигается «окно» длины k : сначала в «окне» находятся первые k чисел,
    на следующем шаге в «окне» уже будут находиться k чисел, начиная со второго,
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

    min_in_step = []

    while True:
        nums = input(f'Введите {length} цифр:')
        nums_array = [int(num) for num in nums.split(' ')]
        if len(nums_array) == length:
            break

        print(f'Нужно ввести {length} цифр')

    for num in range(len(nums_array)):
        if num + step - 1 < len(nums_array):
            step_list = [nums_array[i] for i in range(num, num + step)]
            min_in_step.append(min(step_list))

    return min_in_step


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

    return f'Максимальная хорошесть строки: {len(set(list_input)) - 1}'


def not_three_one_in_a_row():
    """
    По данному числу N определите количество последовательностей
    из нулей и единиц длины N, в которых никакие три единицы не стоят рядом.

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

    return a[length - 1]


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

    for let_1 in range(len(list_string) - 1):

        for let_2 in range(let_1 + 1, len(list_string)):
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
    pots = int(input('Введите количество банок: '))

    while True:
        candy_pots_string = input('Введите количество конфет в банках: ').split(' ')
        if len(candy_pots_string) == pots:
            break

        print(f'Нужно ввести количество конфет в каждой из {pots} банок\n')

    candy_pots = [int(num) for num in candy_pots_string]
    set_pots = set(candy_pots)

    if len(set_pots) <= 2:
        print('Добавлять конфеты не требуется: 0')
        return

    min_candy = min(candy_pots)
    left_part = [min_candy]
    candy_pots.remove(min_candy)

    max_candy = max(candy_pots)
    right_part = [max_candy]
    candy_pots.remove(max_candy)

    for i in range(len(candy_pots)):
        left_val = abs(min_candy - candy_pots[i])
        right_val = max_candy - candy_pots[i]

        if left_val < right_val:
            left_part.append(candy_pots[i])
        else:
            right_part.append(candy_pots[i])

    left_candies = need_candies_at_one_side(left_part)
    right_candies = need_candies_at_one_side(right_part)

    total_min = left_candies + right_candies

    print(f'Нужно добавить конфет: {total_min}')


def need_candies_at_one_side(array: List[int]):
    max_num = max(array)
    summary_left = 0

    for num in range(len(array)):
        summary_left += max_num - array[num]

    return summary_left


class RepeatedNTimes:
    def repeatedNTimes(self, nums: List[int]) -> int:
        rep_times = len(nums) // 2

        count_dict = {}
        for i in range(len(nums)):
            if nums[i] in count_dict:
                count_dict[nums[i]] += 1
            else:
                count_dict[nums[i]] = 1

        for key, value in count_dict.items():
            if value == rep_times:
                return key


class FindSums:
    """
    [2,7,11,15]
    9
    [0, 1]
    [3,2,4]
    6
    [1, 2]
    [3,3]
    6
    [0, 1]
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    answer = [i, j]
                    break

        return answer


def length_of_longest_substring(s: str) -> int:
    if not s:
        return 0

    left = 0
    new_set = set()
    max_length = 0

    for n in range(len(s)):
        if s[n] not in new_set:
            new_set.add(s[n])
            new_max = n - left + 1

            if max_length < new_max:
                max_length = new_max
        else:
            while s[n] in new_set:
                new_set.remove(s[left])
                left += 1

            new_set.add(s[n])

    return max_length


def median_two_arrays(num_1: List[int], num_2: List[int]) -> float:
    nums = num_1 + num_2

    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return (nums[0] + nums[1]) / 2

    if len(num_1) > 0 and len(num_2) > 0:
        left_max = num_1[len(num_1) - 1]
        right_min = num_2[0]

        if left_max > right_min:
            nums = sorted(nums)

    if len(nums) % 2 == 0:
        first_mid = nums[len(nums) // 2 - 1]
        second_mid = nums[len(nums) // 2]
        mid = (first_mid + second_mid) / 2

        return mid
    else:
        mid = nums[len(nums) // 2]
        return mid


def fibonacci_func(n):
    fib_l = [0, 1]

    for i in range(n + 1):
        fib_l.append(fib_l[-1] + fib_l[-2])

    return fib_l


def longest_palindromic_substring(s: str):
    longest_sub_str = ''
    max_str = 0

    if len(s) <= 1:
        return s

    for i in range(len(s) - 1):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                new_sub = s[i:j + 1]

                if new_sub == new_sub[::-1] and max_str < len(new_sub):
                    longest_sub_str = s[i:j + 1]
                    max_str = len(new_sub)

    return longest_sub_str


def search_que(start, graph=None):
    if graph is None:
        return 'No graph added'

    q = deque()
    q.extend(graph[start])
    searched = set()

    while q:
        print(q)
        point = q.popleft()
        print(point)

        if mango_seller(point):
            return f'Found mango seller {point}'
        else:
            q.extend(graph[point])
            searched.add(point)

    return 'No mango seller found'


def mango_seller(name):
    return name[-1] == 'm'


def print_names(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)

    while search_queue:
        dir = search_queue.popleft()
        for file in sorted(listdir(dir)):
            fullpath = join(dir, file)

            if isfile(fullpath):
                print(file)
            else:
                search_queue.append(fullpath)


def printnames(dir):
    for file in sorted(listdir(dir)):
        fullpath = join(dir, file)
        if isfile(fullpath):
            print(file)
        else:
            printnames(fullpath)


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')

            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)


def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    i = 0
    c = 1

    rows = [[] for _ in range(numRows)]

    for char in s:
        rows[i].append(char)

        if i == 0:
            c = 1
        elif i == numRows - 1:
            c = -1

        i += c

    answer = ''.join(''.join(rows[j]) for j in range(len(rows)))

    return answer


def reverse(x: int) -> int:
    x = str(x)[::-1]

    if x[-1] == '-':
        x = int('-' + x[:-1])
    else:
        x = int(x)

    if x not in range(-2 ** 31, 2 ** 31 - 1):
        return 0

    return x


def acid_balance():
    containers = int(input(''))
    volumes = list(map(int, input('').split(' ')))

    if len(volumes) == 1:
        return volumes[0]

    if volumes == sorted(volumes):
        balance = volumes[-1] - volumes[0]
        return balance

    return -1



if __name__ == '__main__':
    array = [5, 25, 1, 11, 31, 17, 2, 14, 8, 16, 4]
    nums = [2, 7, 11, 15]
    # print(convert('PAYPALISHIRING', 4))
    print(acid_balance())
