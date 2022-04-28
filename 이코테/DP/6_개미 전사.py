# 입력
n = int(input())
k = list(map(int, input().split()))

# 특수조건
d = [0] * 100
d[0] = k[0]
d[1] = max(k[0], k[1])

# 실행
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + k[i])

# 출력
print(d[n-1])