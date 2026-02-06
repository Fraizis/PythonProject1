import heapq
from typing import List


def activity_selection(activities):
    """
    activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9)]
    result = activity_selection(activities)

    print("Selected activities:", result)
    """
    activities.sort(key=lambda x: x[1])
    selected = [activities[0]]

    for i in range(1, len(activities)):
        print(activities[i][0], selected[-1][1])
        if activities[i][0] >= selected[-1][1]:
            selected.append(activities[i])

    return selected


def fractional_knapsack(values, weights, capacity):
    """
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    result = fractional_knapsack(values, weights, capacity)

    print("Maximum value in knapsack:", result)
    """
    ratio = [(v / w, v, w) for v, w in zip(values, weights)]
    ratio.sort(reverse=True)

    total_value = 0
    for r, v, w in ratio:
        if capacity >= w:
            capacity -= w
            total_value += v
        else:
            total_value += r * capacity
            break

    return total_value


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(freq_dict):
    heap = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    return heap[0]


def generate_codes(node, code="", huffman_codes=None):
    """
    freq_dict = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
    huffman_tree = build_huffman_tree(freq_dict)
    huffman_codes = generate_codes(huffman_tree)

    print("Character Huffman Codes:")

    for char, code in huffman_codes.items():
        print(f"{char}: {code}")
    """
    if huffman_codes is None:
        huffman_codes = dict()

    if node is None:
        return

    if node.char is not None:  # Leaf node
        huffman_codes[node.char] = code

    generate_codes(node.left, code + "0", huffman_codes)
    generate_codes(node.right, code + "1", huffman_codes)

    return huffman_codes


def set_covering(states_needed, stations):
    """
    states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
    stations = {
        "kone": {"id", "nv", "ut"},
        "ktwo": {"wa", "id", "mt"},
        "kthree": {"or", "nv", "ca"},
        "kfour": {"nv", "ut"},
        "kfive": {"ca", "az"}
    }

    print(set_covering(states_needed, stations))
    """
    final_stations = set()

    while states_needed:
        best_station = None
        states_covered = set()

        for station, states_for_station in stations.items():
            covered = states_needed & states_for_station

            if len(covered) > len(states_covered) and station not in final_stations:
                best_station = station
                states_covered = covered

        if best_station is not None:
            states_needed -= states_covered
            final_stations.add(best_station)
            stations.pop(best_station)
        else:
            return None

    return final_stations


def max_area(height: List[int]) -> int:
    max_vol = 0
    l, r = 0, len(height) - 1

    while l < r:
        print(height[l], height[r])
        side = min(height[l], height[r])
        length = r - l
        max_vol = max(max_vol, side * length)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return max_vol


def isMatch(s: str, p: str) -> bool:
    l = r = 0
    star = -1
    match = 0

    while l < len(s):
        if r < len(p) and (s[l] == p[r] or p[r] == '?'):
            l += 1
            r += 1

        elif r < len(p) and p[r] == '*':
            star = r
            match = l
            r += 1

        elif star != -1:
            r = star + 1
            match += 1
            l = match
        else:
            return False

    while r  < len(p) and p[r] == '*':
        r += 1

    return r == len(p)


if __name__ == "__main__":
    # activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9)]
    # result = activity_selection(activities)
    # print("Selected activities:", result)
    # a, b = map(int, input().strip().split())
    # print(a, b)

    # height = [1,8,6,2,5,4,8,3,7]
    # print(max_area(height=height))
    # print(isMatch(s="aa", p="a"))
    # print(isMatch(s="aa", p="*"))
    # print(isMatch(s="cb", p="?a"))
    print(isMatch(s="cbartyegfbn", p="*a*?bn"))
