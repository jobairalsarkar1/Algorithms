from collections import defaultdict


class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        visited = [False]*(len(self.graph))
        visited[s] = True
        queue = []
        queue.append(s)
        while queue:
            current_node = queue.pop(0)
            # print(current_node)
            print(current_node, end=' ')
            for i in self.graph[current_node]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

# print(g.bfs(2))
g.bfs(2)
