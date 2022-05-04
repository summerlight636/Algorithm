s = input()
n = len(s)

result = int(s[0])
for i in range(1, n):
    if result <= 1 or int(s[i]) <= 1:
        result += int(s[i])
    else:
        result *= int(s[i])

print(result)
