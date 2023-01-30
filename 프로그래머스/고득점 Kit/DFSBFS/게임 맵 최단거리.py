# 반은 통과, 반은 통과 못한 경우 원인: n, m인데 변수에 n, n이 들어가 있어 n==m 인 테스트 케이스만 통과했던 실수였다.
# nx = x + dx[] ny = y + dx[] 실수랑 비슷했다.

from collections import deque


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    visited = [[0] * m for _ in range(n)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque([(0, 0)])
    visited[0][0] = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= n - 1 and 0 <= ny <= m - 1:
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    for x in visited:
        print(x)
    return -1 if visited[n - 1][m - 1] == 0 else visited[n - 1][m - 1]
