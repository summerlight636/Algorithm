def solution(genres, plays):
    answer = []

    genre_play_id = [(genres[i], plays[i], i) for i in range(len(genres))]
    genre_totalPlay_D = {} #딕셔너리 {} 로 생성

    genre_play_id = sorted(genre_play_id, key=lambda x:(x[0],-x[1], x[2])) #sorted와 람다로 정렬

    for t in genre_play_id:
        genre_totalPlay_D[t[0]] = genre_totalPlay_D.get(t[0], 0) + t[1]

    genre_totalPlay_D = sorted(genre_totalPlay_D.items(), key = lambda x:-x[1]) #딕셔너리.items() 이용해서 리스트로 변환 후 정렬

    for genre, totalPlay in genre_totalPlay_D:
        count = 0
        for t in genre_play_id:
            if t[0] == genre:
                count += 1
                answer.append(t[2])
                if count == 2:
                    break
            else:
                if count == 1:
                    break

    print(answer)

    return answer

#다른 사람 풀이 1
def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)): #이렇게 enumerate를 쓰고도 세 변수에 값을 할당  수 있구나.. !!
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer