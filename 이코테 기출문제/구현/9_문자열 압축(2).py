s = "aabbaccc"

def solution(s):
    l = len(s)
    for step in range(1, l//2 + 1):
        count = 1
        now = s[0:step]
        compressed = ""
        for j in range(step, l, step):
            if now == s[j:step+j]:
                count += 1
            else:
                compressed += now if count == 1 else str(count) + now
                now = s[j:step+j]
                count = 1

    return result

print(solution(s))