import sys
input = sys.stdin.readline

#입력
n, m = map(int, input().split())
array = list(map(int, input().split()))

#실행
def binary_search(array, target, start, end):
    array.sort()
    while start <= end:
        mid = (start + end) // 2

        sum = 0
        for i in range(n):
            if i > mid:
                sum += array[i]-array[mid]

        if sum < target:
            end = mid - 1
        else:
            result = array[mid]
            start = mid + 1

    return result

#출력
result = binary_search(array, m, 0, n-1)
print(result)
