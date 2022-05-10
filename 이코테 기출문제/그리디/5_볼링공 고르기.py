n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

#무게/개수 테이블
table = [0]*(m+1)
for v in a:
    table[v] += 1

result = 0
for v in table:
    result += v*(n-v)
    n = n-v

print(result)
