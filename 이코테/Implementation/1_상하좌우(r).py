n = int(input())
plans = list(input().split())

def solutions(n, plans):
    #시작점
    x, y = 1, 1

    #LRUD
    plan_types = ['L', 'R', 'U', 'D']
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for plan in plans:
        for i in range(4):
            if plan == plan_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]

                if 1 <= nx <= n and 1<= ny <= n:
                    x = nx
                    y = ny

    print(x, y)

solutions(n, plans)
