# 임포트/상수
from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 입력
n = int(input())
k = int(input())
board = [[0]*n for _ in range(n)]

#뱀 위치: 1 사과 위치: 2
board[0][0] = 1
for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 2
l = int(input())

#계획 : plan
plan = {}
for _ in range(l):
    x, c = input().split()
    plan[int(x)] = c

print(plan)

# 알고리즘
x, y = (0, 0)
snake = deque([(0, 0)])
direction = 0
time = 0
while True:
    time += 1

    nx = x + dx[direction]
    ny = y + dy[direction]

    if nx < 0 or ny < 0 or nx > n-1 or ny > n-1 or board[nx][ny] == 1:
        x, y = nx, ny
        break

    if board[nx][ny] == 0:
        tx, ty = snake.popleft()
        board[tx][ty] = 0

    board[nx][ny] = 1
    x, y = nx, ny
    snake.append((x, y))

    if time in plan.keys():
        if plan[time] == 'L':
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

# 출력
print(board)
print(time)
