food_times = [3, 1, 2]
k = 5

def solution(food_times, k):
    l = len(food_times)
    i = 0
    time = 0
    while True:
        if time == k:
            print(i+1)
        if food_times[i] != 0:
            food_times[i] -= 1
            time += 1
            i = (i+1) % l

        else:
            i = (i+1) % l

solutions(food_times, k)

