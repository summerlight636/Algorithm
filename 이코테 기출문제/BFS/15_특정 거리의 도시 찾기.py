from collections import deque



n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def solutions(n, k, x, graph):
    INF = 1e9
    dist = [INF] * (n + 1)
    queue = deque([x])
    while queue:
        now = deque.popleft(queue)
        for v in graph[now]:
            if dist[v] == INF:
                dist[v] = dist[now] + 1
                deque.append(v)
            else:
                continue

    count = 0
    for v in dist:
        if v == k:
            count += 1

    result = count
    print(result)

solutions(n, k, x, graph)