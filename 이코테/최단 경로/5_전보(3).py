#
import heapq

#상수
INF = int(1e9)


#입력
n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

#알고리즘
distance = [INF] * (n+1)

def dijkstra(c):
    q = []
    distance[c] = 0
    heapq.heappush(q, (0, c))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for v in graph[now]:
            # v[0]은 도착지점 v[1] 은 거리
            cost = distance[now] + v[1]
            if cost < distance[v[0]]:
                distance[v[0]] = cost
                heapq.heappush(q, (cost, v[0]))

dijkstra(c)

#출력
count = 0
time = 0
for i in range(n+1):
    if distance[i] != INF:
        count += 1
        time = max(time, distance[i])

print(count-1, time)