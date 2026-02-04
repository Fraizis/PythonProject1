def activity_selection(activities):
    # Sort activities by their finish times
    activities.sort(key=lambda x: x[1])
    selected = [activities[0]]  # Always select the first activity

    # Iterate through the activities and select the non-overlapping ones
    for i in range(1, len(activities)):
        print(activities[i][0], selected[-1][1])
        if activities[i][0] >= selected[-1][1]:  # Start time >= last finish time
            selected.append(activities[i])

    return selected


def fractional_knapsack(values, weights, capacity):
    # Create a list of (value-to-weight ratio, value, weight) tuples
    ratio = [(v / w, v, w) for v, w in zip(values, weights)]
    ratio.sort(reverse=True)  # Sort by ratio in descending order

    total_value = 0  # Total value accumulated
    for r, v, w in ratio:
        if capacity >= w:  # If the item fits, take it all
            capacity -= w
            total_value += v
        else:  # Otherwise, take the fractional part of the item
            total_value += r * capacity
            break

    return total_value


import heapq


# Node class to represent tree nodes
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Overriding less than operator for priority queue
    def __lt__(self, other):
        return self.freq < other.freq


# Function to build Huffman Tree
def build_huffman_tree(freq_dict):
    heap = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Extract two nodes with the smallest frequencies
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # Merge these nodes
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Push the merged node back into the heap
        heapq.heappush(heap, merged)

    return heap[0]  # Root of the Huffman tree


# Function to generate Huffman codes
def generate_codes(node, code="", huffman_codes=None):
    if huffman_codes is None:
        huffman_codes = dict()

    if node is None:
        return

    if node.char is not None:  # Leaf node
        huffman_codes[node.char] = code

    generate_codes(node.left, code + "0", huffman_codes)
    generate_codes(node.right, code + "1", huffman_codes)

    return huffman_codes


# Example usage
if __name__ == "__main__":
    # Frequency of characters in the input string
    freq_dict = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}

    # Build Huffman Tree
    huffman_tree = build_huffman_tree(freq_dict)

    # Generate Huffman Codes
    huffman_codes = generate_codes(huffman_tree)

    # Print the Huffman codes
    print("Character Huffman Codes:")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")

    # Example usage
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50
    result = fractional_knapsack(values, weights, capacity)
    print("Maximum value in knapsack:", result)

    # # Example usage
    # activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9)]
    # result = activity_selection(activities)
    # print("Selected activities:", result)
