# 임포트/상수
from collections import deque

# 입력
n, m, k, x = map(int, input().split())
graph = [[]for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

INF = int(1e9)
visited = [False]*(n+1)
distance = [INF]*(n+1)
distance[x] = 0

# 알고리즘
def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        now_node = queue.popleft()
        for next_node in graph[now_node]:
            if not visited[next_node]:
                distance[next_node] = distance[now_node] + 1
                visited[next_node] = True
                queue.append(next_node)

# 출력
bfs(x)

tf = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        tf = True

if tf == False:
    print(-1)


