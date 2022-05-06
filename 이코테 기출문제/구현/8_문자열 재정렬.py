s = input()

num_list = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
l = len(s)

a = []
b = 0
for i in range(l):
    if s[i] in num_list:
        b += int(s[i])
    else:
        a.append(s[i])

a.sort()

for i in a:
    print(i, end='')

print(b)
