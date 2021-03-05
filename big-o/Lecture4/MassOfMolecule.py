n = input()

result = 0
q = []
score = {
    'C': 12,
    'H': 1,
    'O': 16
}
for i in n:
    if i == '(':
        q.append(-1)
    elif i == ')':
        k = 0
        while True:
            tmp = q.pop()
            if tmp == -1:
                break
            else:
                k += tmp
        q.append(k)
    elif i.isdigit():
        q.append(q.pop()*int(i))
    else:
        q.append(score[i])

r = 0
for i in q:
    r += i
print(r)