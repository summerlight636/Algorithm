s = "one4seveneight"

num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def check(s):
    for i in range(10):
        if s == num[i]:
            return str(i)
    return False


def solution(s):
    l = len(s)
    temp = ""
    result = ""

    for i in range(l):
        if s[i].isalpha() == True:
            temp += s[i]
            if len(temp) >= 3:
                if check(temp) != False:
                    result += check(temp)
                    temp = ""
        else:
            result += s[i]

    print(result)
    answer = int(result)
    return answer

print(solution(s))
