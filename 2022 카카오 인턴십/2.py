queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]


def solution(queue1, queue2):
    temp = queue1 + queue2 + queue1
    totalsum = sum(queue1) + sum(queue2)

    if totalsum % 2 != 0:
        return -1
    if sum(queue1) == sum(queue2):
        return 0

    target = totalsum // 2
    l = len(queue1)

    for i in range(2 * l):

        start = 0
        end = (2 * l - 1) - i

        while start <= end:
            mid = (start + end) // 2
            total = sum(temp[i:i + mid])

            if total == target:
                return (i + mid - l) + i
            elif total > target:
                end = mid - 1
            else:
                start = mid + 1

    return -1


print(solution(queue1, queue2))