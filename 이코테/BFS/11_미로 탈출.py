from collections import deque

# 입력값
n,m = map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 함수 정의
count = 0
def BFS(x, y):
    queue = deque([(x, y)])

    while queue:
        (x,y) = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

print(BFS(0, 0))
