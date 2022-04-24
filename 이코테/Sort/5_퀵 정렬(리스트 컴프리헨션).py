def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [i for i in tail if i < pivot]
    right_side = [i for i in tail if i > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

array = [2,3,4,6,1,7]
print(quick_sort(array))
