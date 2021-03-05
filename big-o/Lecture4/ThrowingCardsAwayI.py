n = []
while True:
    tmp = int(input())
    if tmp == 0:
        break
    n.append(tmp)


for i in n:
    queue = [j+1 for j in range(i)]
    dis = []
    while len(queue) > 1:
        dis.append(queue.pop(0))
        queue.append(queue.pop(0))
    if len(dis) > 0:
        print('Discarded cards:', ', '.join(str(x) for x in dis))
    else:
        print('Discarded cards:')
    print('Remaining card:', queue[0])
    