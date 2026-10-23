
def astar(graph, start, goal, h):
    open_list = [(h[start], 0, start, [start])]
    visited = set()

    while open_list:
        open_list.sort()
        f, g, node, path = open_list.pop(0)

        if node == goal:
            print("Path:", path)
            print("Cost:", g)
            return

        if node in visited:
            continue
        visited.add(node)

        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                new_g = g + cost
                new_f = new_g + h[neighbor]
                open_list.append(
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    print("No path found")

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 4)],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

h = {'A': 7, 'B': 6, 'C': 4, 'D': 4,
     'E': 2, 'F': 2, 'G': 0}

astar(graph, 'A', 'G', h)
