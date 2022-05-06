s = input()
l = len(s)

a = 0
b = 0
for i in range(int(l/2)):
    a += int(s[i])
    b += int(s[l - 1 - i])

if a == b:
    print("LUCKY")
else:
    print("READY")