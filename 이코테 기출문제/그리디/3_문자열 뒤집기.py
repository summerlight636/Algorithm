s = input()
n = len(s)

count = 0
for i in range(n-1):
    if s[i] != s[i+1]:
        count += 1

if count % 2 == 0:
    print(int(count/2))
else:
    print(int(count/2 + 1))

