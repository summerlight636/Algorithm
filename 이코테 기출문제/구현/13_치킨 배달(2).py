# 임포트/상수
from itertools import combinations
INF = int(1e9)

# 입력
n, m = map(int, input().split())
city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

chicken = []
house = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i, j))
        elif city[i][j] == 1:
            house.append((i, j))
# 알고리즘
combinations = list(combinations(chicken, m))

min_city_chicken_distance = INF
for comb in combinations:

    city_chicken_distance = 0
    for hx, hy in house:

        chicken_distance = INF
        for cx, cy in comb:
            chicken_distance = min(abs(cx-hx) + abs(cy-hy), chicken_distance)

        city_chicken_distance += chicken_distance

    min_city_chicken_distance = min(min_city_chicken_distance, city_chicken_distance)

# 출력
print(min_city_chicken_distance)
