n = int(input())
dp = [0]*(int(1e9))
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[5] = 1

i = 1
count = 0
result = []
while count < n:
    if dp[i] == 1:
        result.append(i)
        i += 1
        count += 1
        continue
    else:
        if i % 2 == 0:
            if dp[i // 2] == 1:
                result.append(i)
                dp[i] = 1
                count += 1
                i += 1
                continue
        if i % 3 == 0:
            if dp[i // 3] == 1:
                result.append(i)
                dp[i] = 1
                count += 1
                i += 1
                continue
        if i % 5 == 0:
            if dp[i // 5] == 1:
                result.append(i)
                dp[i] = 1
                count += 1
                i += 1
                continue
        i += 1

print(result)