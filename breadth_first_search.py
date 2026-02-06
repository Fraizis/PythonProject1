from collections import deque


def search_que(start, graph=None):
    if graph is None:
        return 'No graph added'

    q = deque()
    q.extend(graph[start])
    searched = set()

    while q:
        print(q)
        point = q.popleft()
        print(point)

        if mango_seller(point):
            return f'Found mango seller {point}'
        else:
            q.extend(graph[point])
            searched.add(point)

    return 'No mango seller found'


def mango_seller(name):
    return name[-1] == 'm'
