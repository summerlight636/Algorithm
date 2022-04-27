def binary_search(array, target, start, end):
    # 재귀니까 종료조건 먼저(실패)
    if start > end:
        return None
    # 성공
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    # 재귀
    elif target < array[mid]:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)