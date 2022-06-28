# 임포트/상수
INF = int(1e9)

# 입력
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 알고리즘
data.sort()
tb = [0] * (m+1)

for v in data:
    tb[v] += 1

result = 0
for i in range(m+1):
    if tb[i] != 0:
        n -= tb[i]
        result += tb[i] * n

# 출력
print(result)
