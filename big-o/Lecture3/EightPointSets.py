points = []

ver = []
hash_ver = {}
max_ver = 0

her = []
hash_her = {}
max_her = 0
for i in range(8):
    point = list(map(int, input().split()))
    points.append(point)

    if not point[0] in ver:
        ver.append(point[0])
        hash_ver[point[0]] = 1
    else:
        hash_ver[point[0]] += 1
        max_ver = max(hash_ver[point[0]], max_ver)

    if not point[1] in her:
        her.append(point[1])
        hash_her[point[1]] = 1
    else:
        hash_her[point[1]] += 1
        max_her = max(hash_her[point[1]], max_her)

if (len(ver) != 3 and len(her) != 3) or max_her > 3 or max_ver > 3:
    print('ugly')
else:
    ver.sort()
    her.sort()
    flag = 0
    for i in points:
        if i == [ver[1], her[1]]:
            flag = 1
            break
    print('respectable' if flag == 0 else 'ugly')