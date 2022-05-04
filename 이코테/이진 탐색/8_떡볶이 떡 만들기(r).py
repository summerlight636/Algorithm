import sys
input = sys.stdin.readline

#입력
n, m = map(int, input().split())
array = list(map(int, input().split()))

#실행
def binary_search(array, target, start, end):
    array.sort()
    mid = (start + end) // 2

    while start <= end:

        sum = 0
        for i in range(n):
            if i > mid:
                sum += array[i]

        if sum == target:
            return mid
        elif sum < target:
            end = mid -1
        else:
            start = mid + 1
    return mid

#출력
result = binary_search(array, m, 0, n-1)
print(result)
