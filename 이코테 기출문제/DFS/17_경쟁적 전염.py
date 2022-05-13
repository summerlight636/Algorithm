from collections import deque

n, k = map(int, input().split())
graph = []
virus = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], 0, i, j))
virus.sort()

s, x, y = map(int, input().split())

#시계
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]

def do(num, time, a, b):
    if time < s:
        for i in range(4):
            na = a + da[i]
            nb = b + db[i]
            if 0 <= na <= n-1 and 0 <= nb <= n-1 and graph[na][nb] == 0:
                graph[na][nb] = num
                q.append((num, time+1, na, nb))
        for x in range(n):
            for y in range(n):
                print(graph[x][y], end=' ')
            print()
    return

q = deque(virus)
while q:
    num, time, a, b = q.popleft()
    do(num, time, a, b)


for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()
print(graph[x-1][y-1])

