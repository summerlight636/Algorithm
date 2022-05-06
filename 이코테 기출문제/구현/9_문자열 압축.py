def solution(s):
    l = len(s)
    answer = len(s)

    for step in range(1, l//2 + 1):
        now = s[0:step]
        compressed = ""

        count = 1
        for j in range(step, l, step):
            if now == s[j:j+step]:
                count += 1
            else:
                compressed += now if count == 1 else str(count) + now
                now = s[j:j+step]
                count = 1

        compressed += now if count == 1 else str(count) + now

        answer = min(answer, len(compressed))
    return answer