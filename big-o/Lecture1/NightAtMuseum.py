s = input()
s = "a" + s
sum = 0

for i in range(0, len(s) - 1):
    if i == len(s) - 1:
        break
    d = abs(ord(s[i+1]) - ord(s[i]))
    if d > 12:
        sum += 25 - d + 1
    else:
        sum += d
print(sum)
