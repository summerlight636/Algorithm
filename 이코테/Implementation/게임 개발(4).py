n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

#북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[0]*m for _ in range(n)]
visited[x][y] = 1

result = 1
tf = True
while tf == True:
    for i in range(4):
        d = (d - 1) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        if visited[nx][ny] == 0 and graph[nx][ny] == 0:
            x = nx
            y = ny
            visited[nx][ny] = 1
            result += 1
            break

        if i == 3:
            nx = x - dx[d]
            ny = y - dy[d]
            if graph[nx][ny] == 1:
                print(result)
                tf = False
                break
            else:
                x = nx
                y = ny