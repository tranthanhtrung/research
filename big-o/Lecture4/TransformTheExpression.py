n = int(input())
arr = [ input() for i in range(n)]

for expression in arr:
    result = ''
    stack = []
    for i in expression:
        if not i in '()+-*/^':
            result += i
        elif i == ')':
            while True:
                if len(stack) == 0:
                    break
                c = stack.pop()
                if c == '(':
                    break
                result += c
        else:
            stack.append(i)

    print(result)