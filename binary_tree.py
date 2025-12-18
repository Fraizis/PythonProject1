class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if root.value == data:
            return root

        if root.value > data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        return root

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.value)
            self.in_order(root.right)

    def get_height(self, root):
        if root is None:
            return 0

        return max(self.get_height(root.left), self.get_height(root.right)) + 1



if __name__ == '__main__':
    tree = Tree()
    root = Node(7)
    tree.insert(root, 3)
    tree.insert(root, 2)
    tree.insert(root, 1)
    tree.insert(root, 9)
    tree.insert(root, 5)
    tree.insert(root, 4)
    tree.insert(root, 6)
    tree.insert(root, 8)

    tree.in_order(root)
    print(tree.get_height(root))
