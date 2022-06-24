from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

visited = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0

def bfs(x, y):
    if visited[x][y] == 1 or graph[x][y] == 1:
        return

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and visited[nx][ny] == 0 and graph[nx][ny] == 0 :
                queue.append((nx, ny))
    global count
    count += 1

for i in range(n):
    for j in range(m):
        bfs(i, j)

print(count)