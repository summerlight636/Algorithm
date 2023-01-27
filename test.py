from itertools import product


lst = [1, 2, 3, 4]
print(lst)
print(*lst)

test = [(1, -1), (2, -2)]
print(product(*test))