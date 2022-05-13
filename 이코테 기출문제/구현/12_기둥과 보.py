def possible(building)
    l = len(building)
    for i in range(l):
        x, y, a = building[i]
        if a == 0:  # 기둥
            if y == 0:
                continue
            elif [x - 1, y, 1] in building or [x, y, 1] in building or [x, y - 1, 0] in building:
                continue
            return False
        else:  # 보
            if [x, y - 1, 0] in building or [x + 1, y - 1, 0] in building or (
                    [x - 1, y, 1] in building and [x + 1, y, 1] in building):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = [[]]

    for x, y, a, do in build_frame:
        if do == 1:  # 설치
            answer += [x, y, a]
            if possible(answer):
                continue
            answer -= [x, y, a]
        elif do == 0:  # 삭제
            answer -= [x, y, a]
            if possible(answer):
                continue
            answer += [x, y, a]

    return answer