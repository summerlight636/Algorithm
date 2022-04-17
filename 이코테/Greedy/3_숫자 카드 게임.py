n, m = map(int, input().split())
result = 0

#한 줄씩 검사
for i in range(n):
  data = list(map(int, input().split()))
  min_value = min(data)
  result = max(min_value, result)

print(result)
