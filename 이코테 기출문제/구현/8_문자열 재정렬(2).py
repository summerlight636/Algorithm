s = input()

def solutions(s):

    result = []
    num = 0
    for v in s:
        if v.isalpha() == True:
            result.append(v)
        else:
            num += int(v)

    result.sort()
    result += str(num)
    print(''.join(result))


solutions(s)