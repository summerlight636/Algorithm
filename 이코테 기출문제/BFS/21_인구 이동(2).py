# 임포트


# 입력
n, l, r = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))

# 상수
INF = int(1e9)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 알고리즘
def dfs(x, y):
    global visited, t_num, t_space, t_list
    visited[x][y] = True
    t_num += A[x][y]
    t_space += 1
    t_list.append((x, y))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx <= n-1 and 0 <= ny <= n-1:
            if not visited[nx][ny] and l <= abs(A[x][y]-A[nx][ny]) <= r:
                dfs(nx, ny)

cond = True
count = 0
visited = [[False]*n for _ in range(n)]
while cond:
    for i in range(n):
        for j in range(n):
            visited[i][j] = False

    cond = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                t_num = 0
                t_space = 0
                t_list = []
                dfs(i, j)
                t_avg = t_num // t_space
                for x, y in t_list:
                    A[x][y] = t_avg
                if t_space != 1:
                    cond = True

    if cond:
        count += 1


# 출력
print(count)
