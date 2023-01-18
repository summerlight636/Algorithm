from collections import deque

n, m = map(int, input().split())

#첫 위치 (1,1) - (0,0)아님 주의
#불가능 0 가능 1
#count = 움직여야하는 최소 칸의 개수 (시작 지점 포함)

miro = []
for _ in range(n):
    miro.append(list(map(int, input())))

for x in miro:
    print(x)

x, y = 0, 0
visited = [[0]*m for _ in range(n)]
visited[x][y] = 1
queue = deque()
queue.append((x, y))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if miro[nx][ny] == 1 and visited[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    if x == n-1 and y == m-1:
        break

print(visited[n-1][m-1])