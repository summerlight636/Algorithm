#플로이드 워셜

#상수
INF = int(1e9)

#입력조건
n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1 ### 까먹을 수 있음!!!
x, k = map(int, input().split())

#초기화
for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0

#수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


#출력조건
distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print('-1')
else:
    print(distance)