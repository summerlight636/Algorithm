a = input()
b = input()

now = 0
count = 0
result = []
for i in range(len(a)):
    temp = now
    tempcount = count

    for j in range(now, len(b)):
        if a[i] == b[j]:
            result += a[i]
            now += 1
            break
        else:
            now += 1
            count += 1
            continue

    if j == len(b) - 1 and i != len(a) - 1:
        result += a[i]
        now = temp
        count = tempcount + 1

print(result)
print(count)