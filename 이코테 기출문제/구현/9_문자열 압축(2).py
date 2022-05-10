s = "aabbaccc"

def solution(s):
    l = len(s)
    result = len(s)
    for step in range(1, l//2 + 1):
        count = 1
        prev = s[0:step]
        compressed = ""
        for j in range(step, l, step):
            if prev == s[j:step+j]:
                count += 1
            else:
                compressed += prev if count == 1 else str(count) + prev
                prev = s[j:step+j]
                count = 1

        compressed += prev if count == 1 else str(count) + prev
        print(step, compressed)
        result = min(result, len(compressed))

    return result

print(solution(s))