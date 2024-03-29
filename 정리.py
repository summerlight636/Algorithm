#해당 문자의 유니코드 값 반환
#ord('a') = 97

#해당 문자가 알파벳인지 확인
#.isalpha()

#리스트를 문자열로 변환
#print(''.join(리스트))

#리스트의 특정 값 개수 반환
count = stages.count(i)

#중간값
(n-1)//2

#리스트 표현
left_side = [x for x in tail if x <= pivot]

#리스트 안에서 특정 값 삭제, 삽입 가능
리스트.append([x, y, a])
리스트.remove([x, y, a])

#리스트(문자열) 안에서 특정 값 조회
리스트.count()

#이진변환
bin() 

#문자열 뒤집기
word = word[::-1]

#특정 값 변환: replace()
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

#count_by_range(a, left, right)
정렬된 리스트에서 값이 left<=x<=right 에 속하는 원소 개수 반환
직접 bisect_right 과 bisect_left 를 이용해 정의하여 ㅅ사용
return right - left 로

#시계 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#n*m의 tmep 그래프 안에서 바이러스
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx <n and 0<= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)

#람다식


# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

#힙 자료구조
출발 노드로부터 가장 거리가 짧은 노드를 빠르게 찾을 수 있음
우선순위 큐: 우서순위 높은 데이터를 가장 먼저 삭제
import heapq
heap = []
heapq.heappush(heap, input)
heapq.heappop(heap)

재귀한도 풀기
import sys
sys.setrecursionlimit(10**7)

내장 :
    1) eval()
    2) sorted(대상, reverse, key)
itertools : 순열과 조합
    data = ['a', 'b', 'c']
    1) result = list(permutations(data, 3)) => [(a,b,c),(a,c,b),(b,a,c),(b,c,a),(c,a,b),(c,b,a) .... 총 3!=6개]
    2) result = list(combinations(data, 2)) => [(a, b), (a, c), (b, c)] 총 3!/2! = 3개
    3) product =  list(product(data,2)) => [(a,a) (a,b )(a,c).... 총 3*3=9개]
    4) combinations_with_replacement = list(combinations_with_replacement(data, 2)) => [(a,a), (a,b), (a,c), (b,b), (b,c), (c,c)] => 중복조합
heapq : 우선순위 큐
bisect : 이진탐색
    1) bisect_left(a,x) : 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스
    2) bisect_right(a,x) : 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스
    정렬된 리스트에서 특정 범위에 속하는 원소의 개수를 빠르게 구할 수 있음
collections : deque, Counter
    1) deque: append, appendleft, pop, popleft
    2) counter = Counter(['a', 'b', 'c', 'b'])
        print(counter['b']) => b가 등장한 횟수 출력
math : 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수, pi 등
    1) factorial(x)
    2) sqrt(x)
    3) gcd(a, b)
    4) math.pi 또는 math.e

#해시
import collections


def solution(participant, completion):
    # 1. participant의 Counter를 구한다
    # 2. completion의 Counter를 구한다
    # 3. 둘의 차를 구하면 정답만 남아있는 counter를 반환한다
    answer = collections.Counter(participant) - collections.Counter(completion)

    # 4. counter의 key값을 반환한다
    return list(answer.keys())[0]


print(solution(["marina", "josipa", "nikola", "vinko", "filipa"]
               , ["josipa", "filipa", "marina", "nikola"]))
출처: https: // coding - grandpa.tistory.com / 85[개발자로
취직하기: 티스토리]

collections.Counter(리스트)
뺄셈 연산 가능

문자열.startswith(문자열)

zip()
동일 개수로 이루어진 자료형을 튜플로 묶어주는 함수
인덱스 짝이 없다면 없는 부분은 버려짐