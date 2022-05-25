import heapq

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

distance = [INF] * (n+1)

q = []
heapq.heappush(q, (0, 1))
distance[1] = 0

while q:
    dist, node = heapq.heappop(q)

    if dist > distance[node]:
        continue

    for v in graph[node]:
        if dist+1 < distance[v]:
            distance[v] = dist+1
            heapq.heappush(q, (dist+1, v))

max_value = 0
result = 0
re = 0
for i in range(1, n+1):
    if distance[i] > max_value:
        max_value = distance[i]
        result = i
        re = 1
    elif distance[i] == max_value:
        re += 1
print(result, max_value, re)