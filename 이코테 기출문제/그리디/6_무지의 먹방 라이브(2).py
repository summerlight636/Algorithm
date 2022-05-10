#남은 시간 순으로 정렬해야 하므로, 우선순위 큐 사용
import heapq
food_times = [3, 1, 2]
k = 5

def solution(food_times, k):
    l = len(food_times)

    q = []
    for i in range(l):
        heapq.heappush(q, (food_times[i], i + 1))

    while heapq.heappop(q)[0] * l <= k:
        k -= heapq.heappop(q)[0] * l
        l -= 1

    return (k % l)

print(solution(food_times, k))
