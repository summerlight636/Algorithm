n = int(input())
a = list(map(int, input().split()))
a.sort()

#target: 가능할 지 판단하고 있는 수
target = 1
for v in a:
    if target < v:
        print(target)
        break
    else:
        target += v