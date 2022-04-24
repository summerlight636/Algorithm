array = [1,6,9,10,10,7]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

result = []
for i in range(len(count)):
    if count[i] != 0:
        result += [i]*count[i]

print(result)