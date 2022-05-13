def balanced_slice(s):
    total = 0
    for i in range(len(s)):
        if s[i] == '(':
            total += 1
        elif s[i] ==')':
            total -= 1
        if total == 0:
            return (s[0:i+1], s[i+1:])

def proper_check(s):
    total = 0
    for i in range(len(s)):
        if s[i] == '(':
            total += 1
        elif s[i] == ')':
            total -= 1
        if total < 0:
            return False
    return True

answer = ''
def solution(p):
    global answer
    if p == '':
        return ''
    u, v = balanced_slice(p)
    print('u:', u, 'v:', v)
    if proper_check(u):
        answer += u
        solution(v)
    else:
        answer += '('
        solution(v)
        answer += ')'
        for x in u[1:len(u)-1]:
            if x == '(':
                answer += ')'
            elif x== ')':
                answer += '('
    return answer

p = "(()())()"
print(solution(p))