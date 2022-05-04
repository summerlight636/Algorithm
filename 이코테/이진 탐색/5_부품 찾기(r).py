import sys
input = sys.stdin.readline

#입력
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

#실행
def binary_search(array, target, start, end):
    a.sort()
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == target:
            return mid
        elif a[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


#출력
for n in b:
    if binary_search(a, n, 0, n-1) != None:
        print("yes", end = ' ')
    else:
        print("no")