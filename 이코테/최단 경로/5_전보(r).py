import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#입력
n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

distance = [INF] * (n+1)

#실행
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)


#출력
count = 0
max = 0
for i in range(1, n+1):
    if distance[i] != INF:
        count += 1
        if max < distance[i]:
            max = distance[i]

print(count, max)