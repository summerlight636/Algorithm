# 임포트
from itertools import combinations

# 입력
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input().split()))

student = []
teacher = []
space = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'S':
            student.append((i, j))
        elif graph[i][j] == 'T':
            teacher.append((i, j))
        else:
            space.append((i, j))

# 알고리즘
# 모든 장애물 설치 케이스에 대하여
for obstacles in list(combinations(space, 3)):
    # 모든 t에 대해 감시 확인
    result = True
    #print(obstacles)
    for tx, ty in teacher:
        # 장애물 먼저 고려해 범위 지정
        x_start = 0
        x_end = n-1
        y_start = 0
        y_end = n-1
        for ox, oy in obstacles:
            if tx == ox:
                if ty < oy:
                    y_end = min(y_end, oy-1)
                else:
                    y_start = max(y_start, oy+1)
            if ty == oy:
                if tx < ox:
                    x_end = min(x_end, ox-1)
                else:
                    x_start = max(x_start, ox+1)

        for i in range(x_start, x_end+1):
            if graph[i][ty] == 'S':
                result = False
        for j in range(y_start, y_end+1):
            if graph[tx][j] == 'S':
                result = False

        #print(x_start, x_end, y_start, y_end)
        if not result:
            break

    if result:
        break


# 출력
print("YES" if result is True else "NO")
