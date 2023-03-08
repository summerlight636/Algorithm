def solution(progresses, speeds):
    #상수
    length = len(progresses)

    #time 배열 만들기
    time = []

    ## 리스트의 개수가 서로 같으므로, zip을 활용하여 for p, s in zip(progresses, speeds): 로 나타냈으면 더 좋았을 것
    ## # progress[i] 와 speeds[i] 가 반복되므로 p, s와 같이 단순하게 나타내는 것이 좋았을 것
    for i in range(length):
        if (100 - progresses[i]) % speeds[i] == 0:
            time.append((100 - progresses[i])//speeds[i])
        else:
            time.append((100 - progresses[i])//speeds[i] + 1)]
        ## 한 줄로 작성 가능하다 : (100-progresses[i])//speeds[i] + ((100-progresses[i])%speeds[i] != 0 and 1)


    #result 배열 만들기
    result = []
    count = 1
    now = time[0]
    for i in range(1, length):
        if now < time[i]:
            result.append(count)
            count = 1
            now = time[i]
        else:
            count += 1
    result.append(count)

    return result

""" 정석 풀이
def solution(progresses, speeds):
    Q=[]
    #zip 사용
    for p, s in zip(progresses, speeds):
        # 처음일 때 len(Q)==0 으로 조건 잡기
        # 방금 값 가져오기: Q[-1]
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            #몫이 2.5일 때 값을 '올림'해야 할 때는 음수로 바꾸어 //
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
"""
