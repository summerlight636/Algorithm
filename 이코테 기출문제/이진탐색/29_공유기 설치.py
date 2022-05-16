n, c = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))
array.sort()


start = 1
end = array[n-1]-array[0]

result = (start + end) // 2
while start <= end:
    mid = (start + end) // 2

    #공유기 몇 개 설치 가능한지
    count = 1
    prev = array[0]
    for i in range(1, n):
        if array[i] >= prev + mid:
            prev = array[i]
            count += 1

    if count < c:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)