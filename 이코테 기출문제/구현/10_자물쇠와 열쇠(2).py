key, lock = [[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def check(graph):
    n = len(graph) // 3
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if graph[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)

    #lock_map 준비
    lock_map = [[0] * (3 * n) for _ in range(3 * n)]
    for i in range(n):
        for j in range(n):
            lock_map[i+n][j+n] = lock[i][j]


    #4번 회전
    for rotation in range(4):

        temp = lock_map
        #시작점: (0~2n-1, 0~2n-1)
        for i in range(2*n):
            for j in range(2*n):
                for a in range(m):
                    for b in range(m):
                        temp[i+a][j+b] += key[a][b]

                if check(temp) == True:
                    return True

                for a in range(m):
                    for b in range(m):
                        temp[i+a][j+b] -= key[a][b]


        key = rotate_a_matrix_by_90_degree(key)

    return False

print(solution(key, lock))