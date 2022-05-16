from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
a = list(map(int, input().split()))

left = bisect_left(a, x)
right = bisect_right(a, x)

count = right - left

if count == 0:
    print(-1)
else:
    print(right - left)


