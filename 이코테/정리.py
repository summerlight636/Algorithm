#해당 문자의 유니코드 값 반환
#ord('a') = 97

#해당 문자가 알파벳인지 확인
#.isalpha()

#리스트를 문자열로 변환
#print(''.join(리스트))

# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

내장 :
    1) eval()
    2) sorted(대상, reverse, key)
itertools : 순열과 조합
    data = ['a', 'b', 'c']
    1) result = list(permutations(data, 3)) => [(a,b,c), .... 총 6개]
    2) result = list(combinations(data, 2)) => [(a, b), (a, c), (b, c)]
    3) product =  list(product(data,2)) => [(a,a) (a,b )(a,c).... 총 9개]
    4) combinations_with_replacement = list(...(data, 2)) => [(a,a), (a,b), (a,c), (b,b), (b,c), (c,c)] => 중복조합
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