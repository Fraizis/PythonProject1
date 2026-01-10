from typing import List


class RecursionDivideAndConquer:
    def div_and_conquer(self, length: int, width: int):
        size = length % width
        if size == 0:
            return width
        else:
            return self.div_and_conquer(length=width, width=size)

    def find_sum_rec(self, arr: List[int]):
        if len(arr) == 0:
            return 0
        elif len(arr) == 1:
            return arr[0]
        else:
            return arr[0] + self.find_sum_rec(arr[1:])

    def find_max_num_req(self, array: List[int]):
        if len(array) == 0:
            return 0
        if len(array) == 1:
            return array[0]
        else:
            max_num = self.find_max_num_req(array[1:])
            return array[0] if array[0] > max_num else max_num

    def count_elements_rec(self, array: List[int]):
        if len(array) == 0:
            return 0
        if len(array) == 1:
            return 1
        else:
            return 1 + self.count_elements_rec(array[1:])
