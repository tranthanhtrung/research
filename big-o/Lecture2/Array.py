[n, k] = list(map(int, input().split()))
arr = list(map(int, input().split()))

hash_arr = {}
r = -1
for i in range(0, n):
    if arr[i] in hash_arr:
        continue
    hash_arr[arr[i]] = 1
    if len(hash_arr) == k:
        r = i
        break

hash_arr = {}
l = -1
for i in range(r, -1, -1):
    if arr[i] in hash_arr:
        continue
    hash_arr[arr[i]] = 1
    if len(hash_arr) == k:
        l = i
        break

if r != -1:
    print(l + 1, r + 1)
else:
    print(-1, -1)
