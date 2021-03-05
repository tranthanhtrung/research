n = int(input())

for k in range(n):
    weight, time, lines = map(int, input().split())
    q = [[],[]]
    result = [0 for i in range(lines)]
    sides = {
        'left': 0,
        'right': 1
    }
    for i in range(lines):
        t, side = input().split()
        q[sides[side]].append([i, int(t)])
    
    cur_time = 0
    cur_side = 0
    
    while len(q[0]) > 0 or len(q[1]):
        if len(q[0]) > 0 and len(q[1]):
            l = q[0][0][1]
            r = q[1][0][1]          
            next_time = min(l, r)
        else:
            next_time = q[0][0][1] if len(q[0]) > 0 else q[1][0][1]
        
        cur_time = max(cur_time, next_time)
        carried = 0

        while len(q[cur_side]) > 0:
            tmp = q[cur_side][0]
            if tmp[1] <= cur_time and carried < weight:
                result[tmp[0]] = cur_time + time
                carried += 1
                q[cur_side].pop(0)
            else:
                break

        cur_side = 1 - cur_side
        cur_time += time
        
    for j in result:
        print(j)
    
    if k != n - 1:
        print()
