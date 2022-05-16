from bisect import bisect_left, bisect_right

n = int(input())
a = list(map(int, input().split()))


def solution(a, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if a[mid] == mid:
        return mid

    elif a[mid] > mid:
        return solution(a, start, mid-1)

    else:
        return solution(a, mid+1, end)

print(solution(a, 0, n-1))