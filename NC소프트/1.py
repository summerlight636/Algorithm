import sys
sys.setrecursionlimit(10**6)

dest = ""
def solution(source):
    global dest

    if source == "":
        return dest

    #source 에서 제거한 알파벳들은 알파벳 순서대로 이어 붙인다.
    temp_dest = []
    temp_source = ""
    for x in source:
        if x not in temp_dest:
            temp_dest.append(x)
        else:
            temp_source += x

    temp_dest.sort()
    for x in temp_dest:
        dest += x

    source = temp_source

    return solution(source)