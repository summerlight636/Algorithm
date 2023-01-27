# 내 풀이
count = 0

def solution(numbers, target):
    global count
    length = len(numbers)

    def dfs(level, sum):
        global count
        if level == length:
            if sum == target:
                count += 1
        else:
            dfs(level+1, sum+numbers[level])
            dfs(level+1, sum-numbers[level])

    dfs(0, 0)

    return count

# 다른 사람 풀이1
# solution 함수 자체를 재귀
# 이 풀이가 가능한 이유는 왼쪽/오른쪽으로 나뉘는 각각의 count의 합이 루트 노드의 count와 같기 때문이다.
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# 다른 사람 풀이2
# 재귀 없이 선택지를 모두 모아 sum을 최종으로 구하고, count(target)으로 계산
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)