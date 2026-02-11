def unique_elems_second_massive():
    nums = input('').split(' ')
    first = set(input('').split(' '))
    second = input('').split(' ')

    answer = [x for x in second if x not in first]
    l = len(answer)
    answer = ' '.join(answer)

    return f'{l}\n{answer}'


if __name__ == '__main__':
    print(unique_elems_second_massive())
