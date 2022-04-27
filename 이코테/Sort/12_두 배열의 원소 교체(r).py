# 입력
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#실행
sum = 0
a = sorted(a)
b = sorted(b, reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

for i in range(n):
    sum += a[i]

#출력
print(sum)