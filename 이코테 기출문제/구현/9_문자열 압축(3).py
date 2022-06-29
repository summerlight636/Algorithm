def solution(s):
    l = len(s)
    min_value = l
    for step in range(1, l // 2 + 1):

        prev = s[0:step]
        count = 1
        compressed = ""
        for j in range(step, len(s), step):
            if prev == s[j:step + j]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                count = 1
                prev = s[j:step + j]

        compressed += str(count) + prev if count >= 2 else prev
        min_value = min(min_value, len(compressed))

    answer = min_value
    return answer