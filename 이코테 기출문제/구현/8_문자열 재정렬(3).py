# 임포트/상수
INF = int(1e9)

# 입력
s = input()

# 알고리즘
a = []
b = 0
for v in s:
    if v.isalpha() == True:
        a.append(v)
    else:
        b += int(v)

a.sort()
if b != 0:
    a.append(str(b))


# 출력
print(''.join(a))
