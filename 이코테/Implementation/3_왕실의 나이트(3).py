input = input()

def solutions(s):
    y = int(ord(s[0])) - int(ord('a')) + 1
    x = int(s[1])

    move_types = [(-1, 2), (-1, -2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

    count = 0
    for v in move_types:
        nx = x + v[0]
        ny = y + v[1]

        if 1<=nx<=8 and 1<=ny<=8:
            count += 1

    print(count)

solutions(input)