#입력
n, m = map(int, input().split())
data = list(map(int, input().split()))
print(data)

#알고리즘
data.sort()

start = 0
end = max(data)

while start <= end:
    mid = (start + end) // 2

    print(start, mid, end)

    #남은 떡 길이 계산
    result = 0
    for v in data:
        if mid < v:
            result += v - mid

    if result < m:
        end = mid -1
    else:
        start = mid + 1
        length = mid

print(length)