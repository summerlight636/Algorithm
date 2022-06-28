# 임포트/상수
import heapq
INF = int(1e9)

# 입력

# 알고리즘
def solution(food_times, k):
    q = []
    l = len(food_times)
    for i in range(l):
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0
    prev = 0
    while sum_value + (q[0][0]-prev) * l <= k :
        now = heapq.heappop(q)[0]
        sum_value += (now - prev) * l
        l -= 1
        prev = now

    result = sorted(q, key=lambda x: x[1])
    return result[(k-sum_value)%length][1]

# 출력
print(result)
