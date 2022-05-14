from itertools import combinations

n = int(input())
graph = []
teachers = []
space = []
for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'T':
            teachers.append((i, j))
        elif graph[i][j] == 'X':
            space.append((i, j))

def check(x, y):
    tx, ty = x, y
    while x >= 0:
        if graph[x][y] == 'O':
            break
        elif graph[x][y] == 'S':
            return True
        x -= 1
    x = tx
    while x < n:
        if graph[x][y] == 'O':
            break
        elif graph[x][y] == 'S':
            return True
        x += 1
    x = tx
    while y >= 0:
        if graph[x][y] == 'O':
            break
        elif graph[x][y] == 'S':
            return True
        y -= 1
    y = ty
    while y < n:
        if graph[x][y] == 'O':
            break
        elif graph[x][y] == 'S':
            return True
        y += 1
    y = ty
    return False

for obstacles in list(combinations(space, 3)):
    #장애물 3개 설치
    for x, y in obstacles:
        graph[x][y] = 'O'

    tf = True
    for x, y in teachers:
        if check(x, y) == True:
            tf = False
            break

    if tf == False:
        for x,y in obstacles:
            graph[x][y] = 'X'
        continue

    print('YES')
    break

if tf == False:
    print('NO')


