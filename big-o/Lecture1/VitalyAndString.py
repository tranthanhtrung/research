s = input()
t = input()

for i in range(len(s) - 1, -1, -1):
    if s[i] == "z":
        s = s[:i] + "a" + s[i+1:]
    else:
        s = s[:i] + chr(ord(s[i]) + 1) + s[i+1:]
        break

print(s if s != t else "No such string")

