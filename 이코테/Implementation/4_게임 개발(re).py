# 변수 입력
n, m = map(int, input().split())
x, y, d = map(int, input().split())

# map: 주어진 맵 입력
imap = []
for i in range(n):
    imap.append(list(map(int, input().split())))

# vmap: visited_map 방문한 맵 초기화
vmap = [[0]*m for _ in range(n)]
vmap[x][y] = 1

# 2차원 이동 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 90도 회전
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

# 시뮬레이션
count = 1
turn_time = 0
while(True):
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    if vmap[nx][ny] == 0 and imap[nx][ny] == 0:
        x = nx
        y = ny
        vmap[nx][ny] = 1 #깜박함
        turn_time = 0  #초기화 해줘야 함
        count += 1
        continue

    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]

        if imap[nx][ny] == 0:
            x = nx
            y = ny
            turn_time = 0

        else:
            break

print(count)





