[n, k] = list(map(int, input().split()))

listPss = [0 for i in range(101)]
for i in range(0, n):
    pss = input()
    listPss[len(pss)] += 1

rPss = input()

countP = 0
for i in range(0, 101):
    if i < len(rPss):
        countP += listPss[i]
    else:
        break

print(countP + 1 + (countP)//k * 5, countP + listPss[len(rPss)] + (countP + listPss[len(rPss)] - 1)//k * 5)
