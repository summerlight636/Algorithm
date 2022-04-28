# 입력
n = int(input())

# 특수조건
d = [0]*1001
d[1] = 1
d[2] = 3

# 실행
for i in range(3, n+1):
    d[i] = (d[i-1] + 2*d[i-2]) % 796796

# 출력
print(d[n])