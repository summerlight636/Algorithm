def solution(participant, completion):
    dict = {}
    sumhash = 0

    for part in participant:
        dict[hash(part)] = part
        sumhash += hash(part)

    for comp in completion:
        sumhash -= hash(comp)

    return dict[sumhash]