def check_relation(net: tuple, first: str, second: str) -> bool | None:
    """
    Дан массив связей пользователей социальной сети.
    Определите, существует ли связь между любыми двумя заданными пользователями.
    Например, если у двух пользователей есть общие друзья или у их друзей есть общие друзья и т.д.

    Ввод: информация о связях, как кортеж (tuple) кортежей; первое имя (str); второе имя (str).

    Вывод: существует ли связь между пользователями (bool).

    :param net: кортеж с именами
    :param first: первое имя
    :param second: второе имя
    :return: Возвращает True если есть общие знакомые,
        иначе False
    """
    for tup in net:
        if first in tup:
            search_name = [name for name in tup if name != first][0]
            print('search_name:', search_name)
            new_net = tuple(elem for elem in net if elem != tup)
            if second == search_name:
                print(f'Matched: {second} == {search_name}')
                return True
            else:
                print(f'Not matched: {second} != {search_name}')
                result = check_relation(new_net, search_name, second)
                if result:
                    return result

    return False


net = (
    ("Ваня", "Лёша"),
    ("Лёша", "Катя"),
    ("Ваня", "Катя"),
    ("Вова", "Катя"),
    ("Лёша", "Лена"),
    ("Оля", "Петя"),
    ("Стёпа", "Оля"),
    ("Оля", "Настя"),
    ("Настя", "Дима"),
    ("Дима", "Маша")
)

if __name__ == '__main__':
    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
