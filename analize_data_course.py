def two_nums_sum():
    n1 = int(input())
    n2 = int(input())
    answer = n1 + n2
    print(answer)


def odd_even():
    n = int(input())
    if n % 2 == 0:
        print('Четное')
    else:
        print('Нечетное')


def quick_sort():
    lst = [5, 3, 2, 1, 4]
    for n in range(len(lst) - 1):
        for i in range(n, len(lst)):
            if lst[n] > lst[i]:
                lst[n], lst[i] = lst[i], lst[n]

    print(lst)


def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)


def dispersion():
    l = [85, 90, 75, 88, 92]
    avg = sum(l) / len(l)

    d = sum((n - avg) ** 2 for n in l) / len(l) - 1
    print(d)


if __name__ == '__main__':
    print()
    l = [18, 20, 22, 19, 21, 17, 23]
    avg = sum(l) / len(l)
    print(avg)
    d = sum((n - avg) ** 2 for n in l) / len(l)
    print(d)
    print(round(d ** 0.5, 2))
