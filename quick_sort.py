from typing import List


class QuickSort:
    def quick_sort(self, array: List[int]):
        if len(array) < 2:
            return array
        else:
            sup_elem = array[0]
            less = [i for i in array[1:] if i <= sup_elem]
            greater = [i for i in array[1:] if i > sup_elem]
            return self.quick_sort(less) + [sup_elem] + self.quick_sort(greater)
