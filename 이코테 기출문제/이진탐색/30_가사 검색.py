from bisect import bisect_left, bisect_right


def count_by_range(a, start, end):
    left = bisect_left(a, start)
    right = bisect_right(a, end)
    return right - left


def solution(words, queries):

    array = [[] for _ in range(10001)]
    array_r = [[] for _ in range(10001)]

    for word in words:
        l = len(word)
        array[l].append(word)
        array_r[l].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        array_r[i].sort()

    answer = []
    for q in queries:
        if q[0] == '?':
            q = q[::-1]
            start = q.replace('?', 'a')
            end = q.replace('?', 'z')
            answer.append(count_by_range(array_r[len(q)], start, end))
        else:
            start = q.replace('?', 'a')
            end = q.replace('?', 'z')
            answer.append(count_by_range(array[len(q)], start, end))

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))