n = int(input())
arr = list(map(int, input().split()))

hash = {}
max_l = 0
cur = 0
j = 0
for i in range(n):
    if not arr[i] in hash:
        hash[arr[i]] = 0
    hash[arr[i]] += 1
    cur += 1

    while len(hash) > 2 and j < n:
        hash[arr[j]] -= 1
        if hash[arr[j]] == 0:
            del hash[arr[j]]
        j += 1 
        cur -= 1
    
    max_l = max(max_l, cur)

print(max_l)