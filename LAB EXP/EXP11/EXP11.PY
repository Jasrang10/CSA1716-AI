
def map_coloring(graph, colors, color_map={}):
    if len(color_map) == len(graph):
        return color_map

    node = next(n for n in graph if n not in color_map)

    for color in colors:
        if all(color_map.get(neighbor) != color
               for neighbor in graph[node]):
            color_map[node] = color

            result = map_coloring(graph, colors, color_map)
            if result:
                return result

            del color_map[node]

    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']
result = map_coloring(graph, colors)

if result:
    print("Map Coloring Solution:")
    for region, color in result.items():
        print(region, ":", color)
else:
    print("No solution exists")
