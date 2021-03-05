def binary_search(arr, value):
  left = 0
  right = len(arr) - 1
  while True:
    if left > right:
      break
    mid = left + (right - left) // 2
    if arr[mid] == value and (mid == left or arr[mid - 1] < arr[mid]):
      return mid
    if value <= arr[mid]:
      right = mid - 1
    else:
      left = mid + 1
  return -1

index = 1
while True:
  n, q = map(int, input().split())
  arr = []
  if n == 0 and q == 0:
    break
  for i in range(n):
    arr.append(int(input()))

  arr.sort()
  print('CASE# ' + str(index) + ':')
  index += 1
  for i in range(q):
    value = int(input())
    result = binary_search(arr, value)
    if result == -1:
      print(value, 'not found')
    else:
      print(value, 'found at', result + 1)