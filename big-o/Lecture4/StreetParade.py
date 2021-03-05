matrix = []
while True:
    n = int(input())
    if n == 0:
        break
    arr = list(map(int, input().split()))
    matrix.append(arr)

for arr in matrix:
    cur = 1
    stack = []
    for i in range(len(arr)):
        if arr[i] == cur:
            cur += 1
        elif len(stack) == 0:
            stack.append(arr[i])
        else:
            while True and len(stack) != 0:
                top = stack.pop()
                if top != cur:
                    stack.append(top)
                    break
                cur += 1
            if cur == arr[i]:
                cur += 1
            else:
                stack.append(arr[i])
    
    while len(stack) > 0:
        if stack.pop() != cur:
            break
        cur += 1

    print('yes' if cur == len(arr) + 1 else 'no')