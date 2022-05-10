#남은 시간 순으로 정렬해야 하므로, 우선순위 큐 사용
import heapq
food_times = [3, 1, 2]
k = 5
def solution(food_times, k):
    l = len(food_times)

    q = []
    for i in range(l):
        heapq.heappush(q, (food_times[i], i + 1))

    sumv = 0
    prev = 0
    while sumv + ((q[0][0]-prev) * l) <= k:
        now = heapq.heappop(q)[0]
        sumv += (now-prev) * l
        l -= 1
        prev = now

    result = sorted(q, key = lambda x:x[1])
    return result[(k -sumv) % l][1]

print(solution(food_times, k))
