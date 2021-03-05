

if __name__ == '__main__'
n = int(input())

arr = []
for i in range(n):
  tmp = input().split(':')
  arr.append({tmp[0]: tmp[1]})

arr.sort(key = lambda item: list(item.keys())[0])

key = input()

left = 0
right = n - 1
while left < right:
  mid = left + (right - left)//2
  if arr[mid] == key