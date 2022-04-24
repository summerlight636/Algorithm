from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def BFS(x, y):
    queue = deque()
    queue.append((x, y))

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]4

    while queue:
        (x, y) = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >=0 and nx<=n-1 and ny<=m-1:
                if not graph[nx][ny] == 0:
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = graph[x][y] + 1
                        queue.append((nx, ny))
    return graph[n-1][m-1]

print(BFS(0,0))