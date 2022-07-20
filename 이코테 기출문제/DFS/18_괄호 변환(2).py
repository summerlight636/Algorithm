# https://school.programmers.co.kr/learn/courses/30/lessons/60058?language=python3
# 임포트/상수

# 입력

# 알고리즘
#여러 번 재사용 하는 경우가 아니라면,
#굳이 def로 선언하기보다는 그냥 본문 코드에 녹아내는 것이 코드가 간결해진다.
def balanced_index(str):
    count = 0
    for i in range(len(str)):
        if str[i] == '(':
            count += 1
        else:
            count -= 1

        if count == 0:
            return i

#여러 번 재사용 하는 경우가 아니라면,
#굳이 def로 선언하기보다는 그냥 본문 코드에 녹아내는 것이 코드가 간결해진다.
def proper(str):
    count = 0
    for i in range(len(str)):
        if str[i] == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(str):
    if str == '':
        return str
    index = balanced_index(str)
    u = str[:index+1] #슬라이싱 범위를 잘못 잡아서, 검토하느라 시간을 낭비했다.
    v = str[index+1:]
    if proper(u):
        return u + solution(v)
    else:
        #이 부분도 한 줄로 쓸 수 있음. 가독성을 위해서가 아니라면!
        """
        result = '('
        result += solution(v)
        result += ')'
        """
        result = '(' + solution(v) + ')'
        #리스트의 모든 부분에 특정 함수 반복 ===> lambda 함수를 쓸 생각을 해야함!
        result += ''.join(list(map(lambda x: ')' if x=='(' else '(', u[1:-1])))
        """
        u = u[1:-1]
        for i in range(len(u)):
            if u[i] == '(':
                result += ')'
            else:
                result += '('
        """
        # 그리고 굳이 result 를 쓸 필요 없이, 바로 return에 쓸 수 있으면 그대로 식을 쓰자.
        return result


# 출력
print(result)

"""
프로그래머스 베스트 풀이 
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                #map(lambda x: '(' if x==')' else ')', p[1:i])
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))
"""