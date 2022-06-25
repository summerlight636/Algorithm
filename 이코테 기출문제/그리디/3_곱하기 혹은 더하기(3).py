# 임포트/상수
INF = int(1e9)

# 입력
s = input()

# 알고리즘
result = int(s[0])
l = len(s)
for i in range(1, l):
    if result <= 1 or int(s[i]) <= 1:
        result += int(s[i])

    else:
        result *= int(s[i])

# 출력
print(result)
