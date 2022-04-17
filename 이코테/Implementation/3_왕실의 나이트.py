start_point = input()
x = int(ord(start_point[0]))-int(ord('a'))+1
y = int(start_point[1])

steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

count = 0
for step in steps:
    nx=x+step[0]
    ny=y+step[1]

    if nx<1 or ny<1 or nx>8 or ny>8:
        continue

    count += 1

print(count)

