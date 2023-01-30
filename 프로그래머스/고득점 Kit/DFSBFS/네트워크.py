# queue에 idx가 아닌 v를 넣는 실수 ..

from collections import deque
def solution(n, computers):
    visited = [0]*n
    count = 0
    for i in range(n):
        if visited[i]!=0 :
            continue
        count += 1
        queue = deque([i])
        while queue:
            x = queue.popleft()
            visited[x] = count
            for idx, v in enumerate(computers[x]):
                if v == 1 and visited[idx] == 0:
                    visited[idx] = count
                    queue.append(idx)

    for x in visited:
        print(x)
    return count