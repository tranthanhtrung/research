n = int(input())
a = list(map(int, input().split()))
sort = a[:]
sort.sort(reverse = True)

curRank = 1
rank = {sort[0]: 1}
doub = 0
for i in range(1, n):
    if not sort[i] in rank:
        curRank += 1 + doub
        rank[sort[i]] = curRank
        doub = 0
    else:
        doub += 1
result = []  
for i in range(n):
    result.append(rank[a[i]])

print(' '.join(str(x) for x in result))