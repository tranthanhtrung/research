n = int(input())
arr = list(map(int, input().split()))

sort = arr[:]
sort.sort()
l = 0
r = 0
for i in range(n):
    if arr[i] != sort[i]:
        l = i
        break
        print(l)

for i in range(n - 1, -1, -1):
    if arr[i] != sort[i]:
        r = i
        break

i = l
j = r
while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1
if arr != sort:
    print('no')
else:
    print('yes')
    print(l + 1, r + 1)