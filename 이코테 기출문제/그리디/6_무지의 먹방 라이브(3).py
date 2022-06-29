# 임포트/상수
import heapq
INF = int(1e9)

# 입력
food_times = [3, 1, 3]
k = 5

# 알고리즘
def solution(food_times, k):

    length = len(food_times)

    if sum(food_times) < k:
        return -1

    #우선순위 큐에 저장
    q = []
    for i in range(length):
        heapq.heappush(q, (food_times[i], i))

    prev = 0
    sum_time = 0
    #온전한 바퀴, 지난 시간 구하기
    while sum_time + (q[0][0] - prev) * length < k:
        sum_time += (q[0][0] - prev) * length
        now = heapq.heappop(q)[0]
        length -= 1
        prev = now

    #남은 바퀴
    q = sorted(q, key= lambda x:x[1])
    return q[(k - sum_time) % (length)][1] + 1

# 출력
print(solution(food_times, k))
