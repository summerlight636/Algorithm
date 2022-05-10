n = int(input())
x = list(map(int, input().split()))
x.sort()

def solution(x):
    result = 0
    count = 0
    for v in x:
        count += 1
        if count >= v:
            result += 1
            count = 0

    return result

print(solution(x))