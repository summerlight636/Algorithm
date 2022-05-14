n = int(input())
a = []
for _ in range(n):
    name, kor, eng, math = input().split()
    a.append((-int(kor), int(eng), -int(math), name))

a.sort()
for i in range(n):
    print(a[i][3])