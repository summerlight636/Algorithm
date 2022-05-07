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

###
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
