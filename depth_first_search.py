import copy
from collections import Counter
from typing import List


class Solution:
    def exist(self, board, word):
        pos = []

        if len(word) == 0:
            return False

        count = 0

        for i in range(len(word)):
            for j in range(len(board)):
                if word[i] in board[j]:
                    count += 1
            if count == 0:
                return False

            count = 0

        for l in range(len(board)):
            if word[0] in board[l]:
                for n in range(len(board[l])):
                    if word[0] == board[l][n]:
                        pos.append([l, n, 1, copy.deepcopy(board)])

                        while pos:
                            # print(pos)
                            next = pos.pop()

                            if next[2] == len(word):
                                return True

                            next[3][next[0]][next[1]] = ''

                            if (next[0] > 0
                                    and next[3][next[0] - 1][next[1]] == word[next[2]]):
                                pos.append([next[0] - 1, next[1], next[2] + 1, copy.deepcopy(next[3])])
                                print('up =', copy.deepcopy(next[3])[next[0] - 1][next[1]])

                            if (next[0] + 1 < len(next[3])
                                    and next[3][next[0] + 1][next[1]] == word[next[2]]):
                                pos.append([next[0] + 1, next[1], next[2] + 1, copy.deepcopy(next[3])])
                                print('down =', copy.deepcopy(next[3])[next[0] + 1][next[1]])

                            if (next[1] > 0
                                    and next[3][next[0]][next[1] - 1] == word[next[2]]):
                                pos.append([next[0], next[1] - 1, next[2] + 1, copy.deepcopy(next[3])])
                                print('left =', copy.deepcopy(next[3])[next[0]][next[1] - 1])

                            if (next[1] + 1 < len(next[3][next[0]]) and
                                    next[3][next[0]][next[1] + 1] == word[next[2]]):
                                pos.append([next[0], next[1] + 1, next[2] + 1, copy.deepcopy(next[3])])
                                print('right =', copy.deepcopy(next[3])[next[0]][next[1] + 1])

        return False


class Solution_1:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols, = len(board), len(board[0])
        board_count = Counter(ch for row in board for ch in row)
        word_count = Counter(word)
        for ch, cnt in word_count.items():
            if board_count[ch] < cnt:
                return False
            if board_count[word[0]] > board_count[word[-1]]:
                word = word[::-1]

        def dfs(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False
            tmp = board[r][c]
            board[r][c] = "#"
            found = (
                    dfs(r + 1, c, i + 1) or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1)

            )
            board[r][c] = tmp
            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        return False


def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')

            for neighbor in reversed(graph[vertex]):
                if neighbor not in visited:
                    stack.append(neighbor)
