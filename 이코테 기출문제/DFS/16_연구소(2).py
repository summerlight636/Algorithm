# 임포트/상수
from itertools import combinations
INF = int(1e9)

# 입력
n, m = map(int, input().split())
jido = []
for i in range(n):
    jido.append(list(map(int, input().split())))

# 상수
space = []
virus_position = []
for i in range(n):
    for j in range(m):
        if jido[i][j] == 0:
            space.append((i, j))
        elif jido[i][j] == 2:
            virus_position.append((i, j))

# 알고리즘
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def virus(x, y):
    jido[x][y] = 2

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<=n-1 and 0<=ny<=m-1:
            if jido[nx][ny] == 0:
                virus(nx, ny)

def count_0(jido):
    count = 0
    for i in range(n):
        for j in range(m):
           if jido[i][j] == 0:
                count += 1
    return count

def simulation():
    result = 0
    for walls in list(combinations(space, 3)):

        for a, b in walls:
            jido[a][b] = 1

        for x, y in virus_position:
            virus(x, y)

        result = max(result, count_0(jido))

        for a, b in space:
            jido[a][b] = 0

    return result

# 출력

print(simulation())
