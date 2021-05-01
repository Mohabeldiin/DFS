def _visit(frontier, graph, fn):
    level = 0
    levels = {}

    while 0 < len(frontier):
        next = []
        for node in frontier:
            fn(node)
            levels[node] = level
            for adj, tree in sorted(graph[node].items()):
                if adj not in levels:
                    next.append(adj)
        frontier = next
        level += 1

def visit(node, graph, fn):
    _visit([node], graph, fn)

graph = {
    0:  {},
    1:  {},
    2:  {},
    3:  {},
    4:  {},
    5:  {},
    6:  {},
    7:  {},
    8:  {},
    9:  {},
    10: {},
    11: {},
    12: {}
}

for edge in [[0,1],[0,2],[1,0],[1,3],[2,4],[2,5],[2,0],[3,1],[4,6],[4,2],[5,2]]:
    graph[edge[0]][edge[1]] = graph[edge[1]]
    graph[edge[1]][edge[0]] = graph[edge[0]]

print(graph)
visited = []
visit(1, graph, (lambda n: visited.append(str(n))))

print(', '.join(visited)) 