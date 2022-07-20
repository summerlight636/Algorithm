# 임포트
INF = int(1e9)

# 입력
n = int(input())
num_list = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 상수
min_result = +INF
max_result = -INF

# 알고리즘
def dfs(result):
    #dfs(result, add, sub, mul, div) 로 함수를 작성했던 것을 dfs(result) 로 수정: global 변수로 지정
    #add, sub, mul, div를 다음 dfs( )에 그대로 넘겨주는 것은 결국 global 변수를 쓰는 것과 동일한 의미이다.
    global max_result, min_result, add, sub, mul, div
    sum_op = add + sub + mul + div
    if sum_op == 0:
        max_result = max(result, max_result)
        min_result = min(result, min_result)

    if add > 0:
        add -= 1
        dfs(result + num_list[-sum_op])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(result - num_list[-sum_op])
        sub += 1
    if mul > 0:
        mul -= 1
        dfs(result * num_list[-sum_op])
        mul += 1
    if div > 0:
        div -= 1
        dfs(int(result / num_list[-sum_op]))
        div += 1

# 출력
dfs(num_list[0])
print(max_result)
print(min_result)

