# 임포트/상수
INF = int(1e9)
import heapq #아쉬운점(1): deque를 쓰는 게 나았다.

# 입력
n, k = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

# 상수
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

heap = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            heapq.heappush(heap, (graph[i][j], i, j))

# 알고리즘
heapq_temp = []
def virus(a, x, y): #아쉬운점(2) 시간 변수를 바이러스 정보에 포함시킬 수 있다는 idea만 있었어도 간단했을 것.
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<=n-1 and 0<=ny<=n-1:
            if graph[nx][ny] == 0:
                graph[nx][ny] = a
                heapq.heappush(heapq_temp, (a, nx, ny))

def simulation(s, x, y):
    time = 0
    global heap, heapq_temp
    while heap:
        a, b, c = heapq.heappop(heap)
        virus(a, b, c)

        if heap == []:
            heap = heapq_temp
            heapq_temp = []
            time += 1
            if time == s:
                return(graph[x-1][y-1])

# 출력
print(simulation(s, x, y))
