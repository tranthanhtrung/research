n = int(input())
a = list(map(int, input().split()))

hash = {}
m = 0
for i in a:
    if not i in hash:
        hash[i] = 0
    hash[i] += 1
    m = max(hash[i], m)

print(m, len(hash))