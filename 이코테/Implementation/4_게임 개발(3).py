n, m = map(int, input().split())
x, y, d = map(int, input().split())

graph = []
for i in range(n):
    a = list(map(int, input().split()))
    graph.append(a)

def turn_left():
    global d
    d = (d - 1) % 4

def solutions(x, y, d, graph):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    turn_time = 0
    graph[x][y] = 1

    result = 0
    while True:
        if turn_time == 4:
            nx = x - dx[d]
            ny = y - dy[d]
            if graph[nx][ny] == 1:
                break

        turn_left()
        turn_time += 1
        nx = x + dx[d]
        ny = y + dy[d]

        if graph[nx][ny] == 0:

            x = nx
            y = ny
            graph[x][y] = 1
            result += 1
            turn_time = 0

    print(result)

solutions(x, y, d, graph)
