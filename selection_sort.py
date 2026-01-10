class SelectionSort:
    def sort_by_select(self, array):
        sorted_arr = []
        for elem in range(len(array)):
            min_elem = self.find_min_elem_in_array(array)
            sorted_arr.append(array.pop(min_elem))

        return sorted_arr

    def find_min_elem_in_array(self, arr):
        min_elem = arr[0]
        min_index = 0
        for i in range(1, len(arr)):
            if arr[i] < min_elem:
                min_elem = arr[i]
                min_index = i

        return min_index
