n, l, r = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))



#
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


visited = [[0]*n for _ in range(n)]
t_num = 0
t_space = 0
t_nation = []


def dfs(x, y):
    global visited, t_num, t_space, t_nation, change
    # print('dfs(', x, ',', y, ')----------')
    if visited[x][y] == 0:
        visited[x][y] = 1
        t_num += graph[x][y]
        t_space += 1
        t_nation.append((x, y))

        for k in range(4):
            # print('k:', k)
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if visited[nx][ny] == 0:
                diff = abs(graph[nx][ny] - graph[x][y])
                if l <= diff <= r:
                    # print(x, ',', y, '에서 ', nx, ',', ny, '방문')
                    dfs(nx, ny)

        if t_num > 1:
            change = True

        # 연합 인구 이동
        for x, y in t_nation:
            graph[x][y] = int(t_num / t_space)

        # print(x, y)
        # print(graph)
        # print(t_nation)

    else:
        return


    #되돌리기
    t_num = 0
    t_space = 0
    t_nation = []


#시뮬레이션
count = 0
dfs(0,0)
print(count)