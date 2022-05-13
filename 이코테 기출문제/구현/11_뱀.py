n = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]

k = int(input())
for i in range(k):
    o, p = map(int, input().split())
    graph[o][p] = 1

l = int(input())
direction = []
for i in range(l):
    x, c = input().split()
    direction.append((int(x), c))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

x = 1
y = 1
d = 0
time = 0
graph[x][y] = 2
q = [(1, 1)]
while True:
    time += 1
    nx = x + dx[d]
    ny = y + dy[d]
    print(nx, ny)
    if 1<= nx <= n and 1<= ny <= n and graph[nx][ny] != 2:
        if graph[nx][ny] == 0:
            a, b = q.pop(0)
            graph[a][b] = 0
        graph[nx][ny] = 2
        q.append((nx, ny))
        x, y = nx, ny
    else:
        x, y = nx, ny

        break

    for t, v in direction:
        if time == t:
            if v == 'L':
                d = (d - 1) % 4
                break
            else:
                d = (d + 1) % 4
                break

print(graph)
print(time)