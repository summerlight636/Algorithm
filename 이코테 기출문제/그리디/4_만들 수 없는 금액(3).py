# 임포트/상수
INF = int(1e9)

# 입력
n = int(input())
data = list(map(int, input().split()))

# 알고리즘
data.sort()

result = 1
for v in data:
    if result < v:
        break
    result += v

# 출력
print(result)
