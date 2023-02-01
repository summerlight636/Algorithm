# 내 풀이
visited = []
minLevel = 0

def solution(begin, target, words):
    global visited
    global minLevel
    words.append(begin)
    visited = [False] * len(words)
    length = len(words)
    minLevel = length

    for i, word in enumerate(words):
        if target == word:
            visited[i] = True
            break
    else:
        return 0

    def dfs(level, now):
        global minLevel
        if level > minLevel:
            return
        if now == begin:
            minLevel = level
            return
        else:
            for i, word in enumerate(words):
                if not visited[i] and isChangeable(word, now):
                    visited[i] = True
                    dfs(level + 1, word)
                    visited[i] = False

    dfs(0, target)

    return minLevel


def isChangeable(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False


# 다른 사람 풀이1
# begin 으로 시작해서, 각각의 단어까지 최소 몇 번 변환해야하는지를 distance 딕셔너리에 저장
# 각각의 리스트에서 한 원소씩 꺼낼 때 zip 활용하기 !!
# yield 활용하기 !
# 딕셔너리를 활용하면 없으면 0 출력이 쉽다
from collections import deque

def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)