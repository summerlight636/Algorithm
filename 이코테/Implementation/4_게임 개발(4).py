n, m = map(int, input().split())
x, y, d = map(int, input().split())

jido = []
for _ in range(n):
    jido.append(list(map(int, input().split())))


#첫 칸은 1,1
#북 동 남 서
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

#방문한 칸
visited = [[0]*n for _ in range(m)]
visited[x][y] = 1

def turn_left(d):
    print((d-1)%4)
    return (d-1)%4

turn_time = 0
count = 1
while True:
    d = turn_left(d)
    turn_time += 1
    nx = x + dx[d]
    ny = y + dy[d]
    print(nx, ny)
    if (jido[nx][ny] == 0) and (visited[nx][ny] == 0):
        x = nx
        y = ny
        visited[x][y] = 1
        count += 1
        turn_time = 0
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if jido[nx][ny] == 1:
            break
        x = nx
        y = ny
        visited[x][y] = 1
        turn_time = 0

print(visited)
print(count)