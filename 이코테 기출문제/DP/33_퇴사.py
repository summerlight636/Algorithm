n = int(input())
array = [(0, 0)]
for i in range(n):
    t, p = map(int, input().split())
    array.append((t, p))

dp = [0]*(n+2)
dp[0] = 0
dp[1] = 0
for i in range(2, n+2):
    value = dp[i-1]
    for j in range(1, i):
        if array[j][0] + j == i:
            value = max(value, dp[j]+array[j][1])
    dp[i] = value

print(dp[n+1])
