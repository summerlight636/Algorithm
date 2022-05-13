from itertools import permutations

def solution(n, weak, dist):
    answer = 0

    #취약 지점 원형->일자
    l = len(weak)
    for i in range(l):
        weak.append(weak[i] + l)

    #시뮬레이션
    result = len(dist) + 1
    for start in range(l): #i: 시작점
        for pset in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + pset[count-1]
            for i in range(start, start+l):
                if position < weak[i]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[i] + pset[count-1]
            print(start, pset, count)
            result = min(result, count)

    if result > len(dist):
        return -1

    answer = result
    return answer