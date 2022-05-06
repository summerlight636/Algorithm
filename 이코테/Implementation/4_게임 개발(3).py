n, m = map(int, input().split())
x, y, d = map(int, input().split())

graph = []
for i in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

def turn_left(d):
    result = (d-1) % 4
    return result

def solutions(n, m, x, y, d, graph):
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    turn_time = 0
    result = 1
    while True:
        d = turn_left(d)
        nx = x + dx[d]
        ny = y + dy[d]

        if visited[nx][ny] == 0 and graph[nx][ny] == 0:
            x = nx
            y = ny
            visited[x][y] = 1
            result += 1
            turn_time = 0
            continue
        else:
            turn_time += 1

        if turn_time == 4:
            nx = x - dx[d]
            ny = y - dy[d]

            if graph[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0

    print(result)

solutions(n, m, x, y, d, graph)
