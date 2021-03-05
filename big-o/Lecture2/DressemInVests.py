[n_soldiers, n_vests, x, y] = list(map(int, input().split()))
soldiers = list(map(int, input().split()))
vests = list(map(int, input().split()))

result = []

j = 0
i = 0
while i < n_soldiers and j < n_vests:
    if soldiers[i] - x > vests[j]:
        j += 1
        continue
    if soldiers[i] + y < vests[j]:
        i += 1
        continue
    result.append([i+1, j+1])
    j += 1
    i += 1

print(len(result))
for i in result:
    print(i[0], i[1])
