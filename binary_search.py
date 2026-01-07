from typing import List


class BinarySearch:
    def binary_search_train_array(self, str_1, str_2):
        """
        Формат ввода
        В первой строке входных данных содержатся натуральные
        числа N и K. Во второй строке задаются N
        элементов первого массива, а в третьей строке – K элементов
        второго массива. Элементы обоих массивов - целые числа

        Формат вывода
        Требуется для каждого из K чисел вывести в отдельную строку "YES",
        если это число встречается в первом массиве, и "NO" в противном случае.
        """
        array_1 = sorted(list(map(int, str_1.split(' '))))
        array_2 = sorted(list(map(int, str_2.split(' '))))

        for num in array_2:
            print(self.binary_search_recursion(num, array_1, 0, len(array_1) - 1))

    def binary_search(self, num: int, array: List[int]):
        array = sorted(array)

        low = 0
        high = len(array) - 1

        while low <= high:
            mid = (low + high) // 2
            search = array[mid]

            if search == num:
                return 'YES'

            elif search > num:
                high = mid - 1
            else:
                low = mid + 1

        return 'NO'

    def binary_search_recursion(
            self,
            search: int,
            array: List[int],
            left: int,
            right: int,
    ):
        if left > right:
            return 'NO'

        mid = (left + right) // 2
        guess = array[mid]

        if guess == search:
            return 'YES'

        if guess > search:
            return self.binary_search_recursion(search, array, left, mid - 1)
        else:
            return self.binary_search_recursion(search, array, mid + 1, right)


if __name__ == '__main__':
    bin_s = BinarySearch()
