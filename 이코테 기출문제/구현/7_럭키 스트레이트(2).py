n = input()

def solutions(n):
    l = len(n)

    sum1 = 0
    for i in range(int(l/2)):
        sum1 += int(n[i])

    sum2 = 0
    for i in range(int(l/2), l):
        sum2 += int(n[i])

    if sum1 == sum2:
        print("LUCKY")
    else:
        print("READY")

solutions(n)