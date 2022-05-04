n, m = map(int, input().split())
k = list(map(int, input().split()))
k.sort()
x = set(k)

d = [0]*11

for v in k:
    d[v] += 1

count = 0
for i in k:
    for j in range(i+1, 10):
        if d[j] != 0:
            count += d[j]

print(count)