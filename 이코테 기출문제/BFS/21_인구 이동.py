n, l, r = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))



#
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


temp = [[0]*n for _ in range(n)]
t_num = 0
t_space = 0
t_nation = []
change = False
def dfs(x, y):
    global temp, t_num, t_space, t_nation, change
    temp[x][y] = 1
    t_num += graph[x][y]
    t_space += 1
    t_nation.append((x, y))

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        diff = abs(graph[nx][ny]-graph[x][y])
        if nx < 0 or nx >= n or ny < 0 or ny >= n or diff < l or diff > r or temp[nx][ny] == 1:
            return
        else:
            dfs(nx, ny)

    if t_num > 1:
        change = True

    #연합 인구 이동
    for x, y in t_nation:
        graph[x][y] = int(t_num / t_space)

    #되돌리기
    temp = [[0]*m for _ in range(n)]
    t_num = 0
    t_space = 0
    t_nation = []


#시뮬레이션
count = 0
while True:
    for i in range(n):
        for j in range(n):
            dfs(i, j)

    if change == False:
        break

    elif change == True:
        count += 1
        change = False

print(count)