#입력
n, m = map(int, input().split())
data = list(map(int, input().split()))

#실행
def left(height):
    sum = 0
    for i in data:
        diff = i - height
        if diff > 0:
            sum += diff
    return sum

start = 0
end = max(data)
while start >= end:
    mid = (start + end) // 2
    if left(mid) == m:
        print(mid)
    elif left(mid) < m:
        start = mid + 1
    else:
        end = mid - 1
