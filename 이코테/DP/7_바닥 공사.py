# 입력
n = int(input())

# 특수조건
d = [0]*1000
d[0] = 1
d[1] = 3

# 실행
for i in range(2, n):
    d[i] = (d[i-1] + 2*d[i-2]) % 796796

# 출력
print(d[n-1])