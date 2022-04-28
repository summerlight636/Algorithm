# 입력
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

# 특수 조건
d = [10001] * (m+1)
d[0] = 0

# 실행
for i in range(n):
    for j in range(a[i], m+1):
        if d[j-a[i]] != 10001:
            d[j] = min(d[j], d[j-a[i]] + 1)

#
# 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])