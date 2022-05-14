n = int(input())
a = list(map(int, input().split()))

a.sort()
print(a)
l = len(a)

if l%2 == 0:
    print(a[l//2 -1])
else:
    print(a[l//2])