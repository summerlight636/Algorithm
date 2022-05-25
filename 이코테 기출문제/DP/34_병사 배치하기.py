n = int(input())
a = list(map(int, input().split()))

dp = [0]*(n+1)
dp[0] = 0
dp[1] = a[0]

count = 0
for i in range(2, n):
    if a[i-1] < a[i]:
        count += 1

print(count)
