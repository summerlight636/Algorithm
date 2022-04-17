input = input()
column = int(ord(input[0]))-int(ord('a')) + 1
row = int(input[1])

step_types = [(-2, 1), (-2, -1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, 2), (-1, -2)]

result = 0
for step in step_types:

    ncolumn = column + step[0]
    nrow = row + step[1]

    if nrow<1 or ncolumn<1 or nrow>8 or ncolumn>8:
        continue

    result += 1

print(result)
