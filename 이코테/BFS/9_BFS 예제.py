from collections import deque

def BFS(graph, v, visited):
    queue = deque(v)
    visited[v] = True

    while queue:
        v = popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = []
