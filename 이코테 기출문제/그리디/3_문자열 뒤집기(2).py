s = input()
l = len(s)

count = 0 #달라지는 횟수
for i in range(l-1):
    if s[i] != s[i+1]:
        count += 1

if count % 2 == 0 :
    print(count//2)
else:
    print(count//2 + 1)
