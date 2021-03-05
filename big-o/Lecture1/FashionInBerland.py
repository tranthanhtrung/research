n = int(input())
a = list(map(int, input().split()))

sum = 0
if len(a) == 1 and a[0] == 0:
    print("NO")
elif len(a) == 1 and a[0] == 1:
    print("YES")
else:
    for i in a:
        if i == 0:
            sum += 1
    print("YES" if sum == 1 else "NO")

