n, m, k = map(int, input().split())
input_list = list(map(int, input().split()))

input_list.sort()
first = input_list[n-1]
second = input_list[n-2]

result = 0
while True:
    for i in range(k):
        if m > 0:
            m -= 1
            result += first

        elif m == 0:
            break

    if m == 0:
        break

    result += second
    m -= 1

print(result)