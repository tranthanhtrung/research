tc = 1
while True:
    [p, c] = list(map(int, input().split()))
    if [p, c] == [0, 0]:
        break

    result = []
    q = [i + 1 for i in range(min(p, c))]
    for i in range(c):
        line = input().split()
        if line[0] == 'N':
            val = q.pop(0)
            result.append(val)
            q.append(val)
        else:
            if int(line[1]) in q:
                q.remove(int(line[1]))
            q.insert(0, int(line[1]))
    
    print('Case {}:'.format(tc))
    tc += 1
    for i in result:
        print(i)