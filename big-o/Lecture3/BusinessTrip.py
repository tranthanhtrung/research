k = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)

result = 0
for i in range(12):
    if k <= 0:
        break
    result += 1
    k -= a[i]

print(result if k <= 0 else -1)