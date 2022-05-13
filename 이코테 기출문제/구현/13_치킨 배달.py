from itertools import combinations

n, m = map(int, input().split())
graph = []
house = []
chicken = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

def simulation():
    comb = list(combinations(chicken, m)) #m개의 치킨집

    result = 1e9
    for cset in comb:
        total_distance = 0
        for h in house:
            hx, hy = h
            distance = 1e9
            for c in cset:
                cx, cy = c
                distance = min(distance, abs(hx-cx)+abs(hy-cy)) #한 집의 치킨거리
            total_distance += distance
        result = min(result, total_distance)
    return result

print(simulation())