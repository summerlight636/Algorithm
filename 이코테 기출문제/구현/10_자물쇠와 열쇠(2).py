key, lock = [[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def check(lock_map):
    n = len(lock_map) // 3
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if lock_map[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    #lock_map 준비
    lock_map = [[0] * (3 * n) for _ in range(3 * n)]
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            lock_map[i][j] = lock[i-n][j-n]

    result = False
    temp = lock_map
    #4번 회전
    for i in range(4):
        #시작점: (n~2n-1, n~2n-1)
        for i in range(n, 2*n):
            for j in range(n, 2*n):
                for a in range(0, m):
                    for b in range(0, m):
                        temp[i+a][j+b] += key[a][b]

        if check(temp) == True:
            return True

        else:
        #만족하지 못할 경우, 회전
            temp = lock_map
            rotate_a_matrix_by_90_degree(key)

    return result

print(solution(key, lock))