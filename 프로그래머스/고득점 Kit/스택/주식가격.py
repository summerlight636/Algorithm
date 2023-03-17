#n이 10^5로 크니까, 효율성 생각해야한다.
def solution(prices):
    answer = []

    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j - i)
                break
            if j == len(prices) - 1:
                answer.append(j - i)

    answer.append(0)
    return answer