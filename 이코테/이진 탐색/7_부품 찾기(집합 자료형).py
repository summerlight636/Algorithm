import sys
input = sys.stdin.readline

#입력
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

#실행
a = set(a)

#출력
for v in b:
    if v in a:
        print("yes", end=' ')
    else:
        print("no", end=' ')
