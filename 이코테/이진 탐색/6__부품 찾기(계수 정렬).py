import sys
input = sys.stdin.readline

#입력
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

#실행
array = [0] * 1000001
for x in a:
    array[x] = 1

#출력
for x in b:
    if array[x] == 1:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')
