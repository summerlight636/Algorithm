def solution(key, lock):
    m = len(key)
    n = len(lock)

    graph = extend_graph(lock, 3)

    # 시작점은 (i, j) = (0~2n, 0~2n)
    for i in range(2 * n):
        for j in range(2 * n):
            # 네 가지 방향
            for k in range(4):

                for a in range(m):
                    for b in range(m):
                        graph[i + a][j + b] += key[a][b]

                if check(graph) == True:
                    return True

                for a in range(m):
                    for b in range(m):
                        graph[i + a][j + b] -= key[a][b]

                key = rotate_key(key)

    return False


def rotate_key(graph):
    m = len(graph)
    result = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            result[m - 1 - j][i] = graph[i][j]
    return result


def extend_graph(graph, size):
    n = len(graph)
    result = [[0] * (size * n) for _ in range(size * n)]
    for i in range(n):
        for j in range(n):
            result[n + i][n + j] = graph[i][j]
    return result


def check(extended_graph):
    n = (len(extended_graph)) // 3
    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            if extended_graph[i][j] != 1:
                return False
    return True


