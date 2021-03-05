s = input()
t = input()

countS = {}
countT = {}

for i in range(0, len(s)):
    if not s[i] in countS:
        countS[s[i]] = 0
    countS[s[i]] += 1

for i in range(0, len(t)):
    if not t[i] in countT:
        countT[t[i]] = 0
    countT[t[i]] += 1

isRemove = False
isNeedTree = False
isSwap = False

isRemove = len(countS) > len(countT)

for i in countT:
    if not i in countS:
        isNeedTree = True
        break
    elif countT[i] > countS[i]:
        isNeedTree = True
        break
    elif countT[i] < countS[i]:
        isRemove = True

match = -1
index = 0
for i in t:
    index = s.find(i, match + 1)
    if index > match:
        match = index
    else:
        isSwap = True
        break

if isNeedTree:
    print('need tree')
elif isRemove and isSwap:
    print('both')
elif not isRemove:
    print('array')
else:
    print('automaton')
