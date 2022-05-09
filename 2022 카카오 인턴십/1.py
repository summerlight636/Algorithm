queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]


def solution(queue1, queue2):
    temp = queue1 + queue2
    totalsum = sum(queue1) + sum(queue2)

    if totalsum % 2 != 0:
        return -1
    if sum(queue1) == sum(queue2):
        return 0

    target = totalsum // 2
    l = len(queue1)

    for i in range(2 * l):
        table = [0]*(2*l)
        for j in range(2*l-i):
            if i==0 and j==0:
                table[i+j] = temp[0]
            else:
                if j == 0:
                    table[i+j] = temp[i]
                else:
                    table[i+j] = table[i+j-1] + temp[i+j]
                    if table[i+j] == target:
                        print(table)
                        return (i + j - l) + i + 1
        print(table)
        print(target)
    print(temp)
    return -1



print(solution(queue1, queue2))