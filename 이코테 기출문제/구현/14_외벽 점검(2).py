# 임포트/상수
from itertools import permutations

# 알고리즘
def solutions(n, weak, dist):
    weak_length = len(weak)

    #원형 -> 일자
    for i in range(lweak_length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1
    #시작지점*친구순서 모든 경우에 대하여
    for start in range(weak_length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[0]

            for index in range(start, start+length):
                if position >= weak[index]:
                    continue
                if count == len(dist):
                    count += 1
                    break
                count +=1
                position = weak[index] + friends[count - 1]

            answer = min(answer, count)

    if answer > len(dist):
        return -1
    return answer


