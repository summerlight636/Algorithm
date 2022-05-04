import sys
input = sys.stdin.readline
INF = 10001

#입력
n, m = map(int, input().split())

array = []
for _ in range(n):
    array.append(int(input()))

d = [10001] * (m+1)
d[0] = 0

for i in range(m+1):
    for v in array:
        if i % v == 0:
            d[i] = min(d[i], i//v)

        d[i] = min(d[i], d[i-v] + 1)

print(d[m])