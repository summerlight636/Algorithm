n, k = map(int, input().split())

array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))

array_A.sort()
array_B.sort()

for i in range(k):
    if array_A[i] < array_B[n-1-i]:
        array_A[i], array_B[n-1-i] = array_B[n-1-i], array_A[i]

sum = 0
for i in range(n):
    sum += array_A[i]

print(sum)
