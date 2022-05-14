def solution(N, stages):
    answer = []

    failure_rate = [0] * (N + 2)

    result = []
    for i in range(1, N + 1):
        total = 0
        for j in range(i, N + 2):
            total += challenging[j]
        if total == 0:
            failure_rate[i] = 0
        else:
            failure_rate[i] = challenging[i] / total
        result.append((i, failure_rate[i]))

    result = sorted(result, key = lambda x:x[1], reverse=True)
    for i in range(len(result)):
        answer.append(result[i][0])
    return answer