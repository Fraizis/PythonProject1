import random
import string
import time
from typing import List


def reverse_str(string: str) -> str:
    return string[::-1]


def longest_word_in_string(string: str) -> str:
    lst_str = string.split(' ')
    max_len = max(lst_str, key=len)

    return max_len


def check_if_palindromic(string: str) -> bool:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    string = string.lower()
    new_str = ''

    if string.isalnum():
        return string == string[::-1]

    for i in string:
        if i in alphabet:
            new_str += i

    if new_str == new_str[::-1]:
        return True

    return False


def find_sum_in_array(list_nums: List) -> int | float:
    start = time.time()

    summ = 0

    for i in list_nums:
        if isinstance(i, (int, float)) and not isinstance(i, bool):
            summ += i

    print((time.time() - start) * 1000)

    return summ


def remove_dublicats(array: List) -> List:
    new_array = []

    for i in array:
        if i not in new_array:
            new_array.append(i)

    return new_array


def count_words_in_string(string: str):
    symbols = '!@#$%^&*()_+=-`~[]{}|;:",./<>?'
    string = string.lower()
    new_str = string.split(' ')
    dict_rep = dict()

    if string == '' or string == ' ':
        return dict_rep

    for i in range(len(new_str)):
        if not new_str[i].isalnum():
            new_str[i] = ''.join([l for l in new_str[i] if l not in symbols])

    for k in new_str:
        if k in dict_rep.keys():
            dict_rep[k] += 1
        else:
            dict_rep[k] = 0

    return dict_rep


def generate_password(count: int):
    symbols = string.ascii_letters + string.punctuation
    password = ''.join(random.choice(symbols) for i in range(count))
    return password


def fact(num: int) -> int | None:
    if num < 0:
        return None

    elif num <= 1:
        return 1

    return num * fact(num - 1)


def number_is_prime(num: int) -> bool:
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def domain_name(string: str) -> str:
    if '://' in string:
        string = ''.join(string.split('://')[1:])

    print(string)
    if string.startswith('www.'):
        string = data[4:]
        range_num = string.find('com')
        return ''.join(string[:range_num + len('com')])

    return ''.join(string.split('://')[1:])


if __name__ == '__main__':
    data = 'www.poisk.com/search?q=python'
    print(domain_name(data))
