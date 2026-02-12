def unique_elems_second_massive():
    nums = ['4', '8']
    first = {'1', '2', '3', '1'}
    second = ['5', '1', '0', '7', '0']

    answer = [x for x in second if x not in first]
    l = len(answer)
    answer = ' '.join(answer)

    return f"""{l}
{answer}"""


if __name__ == '__main__':
    print(unique_elems_second_massive())
