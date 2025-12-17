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


if __name__ == '__main__':
    # bracket_order()
    # count_words_in_text()
    synonym_dict()
