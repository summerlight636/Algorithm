n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            array[i][j] += array[i-1][j]
            continue
        elif j == i:
            array[i][j] += array[i-1][j-1]
            continue
        array[i][j] += max(array[i-1][j-1], array[i-1][j])

result = 0
for i in range(n):
    result = max(array[n-1][i], result)

print(array)
print(result)