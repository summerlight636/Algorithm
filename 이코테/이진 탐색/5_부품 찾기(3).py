import sys
input = sys.stdin.readline

#입력
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

#알고리즘

# 이진탐색을 위해서, 정렬
a.sort()

#이진탐색
def binary_search(a, start, end, target):

    while start <= end:
        mid = (start + end) // 2

        if target > a[mid]:
            start = mid + 1
            binary_search(a, start, end, target)
        elif target < a[mid]:
            end = mid - 1
            binary_search(a, start, end, target)
        elif target == a[mid]:
            return mid


    return -1

#출력
for v in b:
    if binary_search(a, 0, len(a)-1, v) == -1:
        print("no", end=' ')
    else:
        print("yes", end=' ')



