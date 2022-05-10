s = input()

def solution(s):

    result = 0
    for i in range(0, len(s)):
        if result <= 1 or int(s[i]) <= 1:
            result += int(s[i])
        else:
            result *= int(s[i])
    return result

print(solution(s))