from collections import deque



n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def solutions(n, k, x, graph):
    INF = int(1e9)
    dist = [INF] * (n + 1)
    dist[x] = 0
    queue = deque([x])
    while queue:
        now = queue.popleft()
        for v in graph[now]:
            if dist[v] == INF:
                dist[v] = dist[now] + 1
                queue.append(v)

    check = False
    for i in range(1, n+1):
        if dist[i] == k:
            print(i)
            check = True

    if check == False:
        print(-1)


solutions(n, k, x, graph)