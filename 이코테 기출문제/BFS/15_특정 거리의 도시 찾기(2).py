from collections import deque

#단방향
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

INF = 1e9
distance = [INF]*(n+1)
distance[x] = 0
q = deque([x])
#시뮬레이션
while q:
    now = q.popleft()
    for v in graph[now]:
        if distance[v] == INF:
            q.append(v)
            distance[v] = distance[now] + 1

#출력
tf = False
for i in range(n+1):
    if distance[i] == k:
        print(i)
        tf = True
if tf == False:
    print(-1)