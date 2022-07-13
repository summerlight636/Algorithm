# 임포트/상수
from itertools import permutations
from collections import deque

# 알고리즘def solutions:
perm = permutations(dist, len(dist))

min_value = 8
for p in perm:
    p = deque(p)
    count = 0
    dist = 0
    for w in weak:
        if dist < w:
            power = p.popleft()
            count += 1
            dist = w + power
        else:
            continue
    min_value = min(min_value, count)

# 출력
print(min_value)
