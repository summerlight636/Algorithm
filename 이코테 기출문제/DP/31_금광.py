t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    graph = []
    index = 0
    for i in range(n):
        graph.append(a[index:index+m])
        index += m

    result = [[0]*m for _ in range(n)]
    for i in range(n):
        result[i][0] = graph[i][0]
    answer = 0
    for j in range(1, m):
        for i in range(n):
            result[i][j] = result[i][j-1]
            if i-1 >= 0:
                result[i][j] = max(result[i][j], result[i-1][j-1])
            if i+1 < n:
                result[i][j] = max(result[i][j], result[i+1][j-1])
            result[i][j] += graph[i][j]
            answer = max(answer, result[i][j])

    print(answer)