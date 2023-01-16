#특정 지점에서 일이 완료되었음을 나타내는 dfs() == True 활용
n, m = map(int, input().split())
graph = []
#띄어쓰기 없이 주어지는 경우 split 없이 input을 입력
for _ in range(n):
    graph.append(list(map(int, input())))

visited = [[0]*m for _ in range(n)]
count = 0
print(visited)

def dfs(x, y):
    global visited
    if x<0 or x>=n or y<0 or y>=m:
        return
    if visited[x][y] == 0 and graph[x][y] == 0:
        visited[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and graph[i][j] == 0:
            count += 1
            dfs(i, j)

print(count)
