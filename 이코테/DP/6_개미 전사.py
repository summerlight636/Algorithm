# 입력
n = int(input())
k = list(map(int, input().split()))
a = [0]*(n+1)

# 특수조건
a[1] = k[0]
a[2] = max(k[0], k[1])

# 실행
for i in range(3, n+1):
    a[i] = max(a[i-2]+k[i-1], a[i-1])

# 출력
print(a[n])