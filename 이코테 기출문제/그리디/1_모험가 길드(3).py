# 입력
n = int(input())
data = list(map(int, input().split()))

#알고리즘
data.sort()

result = 0
count = 0
for v in data:
    count += 1
    if count >= v:
        result +=1
        count = 0

#출력
print(result)