n = int(input())
a = list(map(int, input().split()))

duration = 0

for i in range(0, n):
    if a[0] > 15:
        duration = 15
        break
    if i == n - 1:
        duration = a[i] + 15
        break
    if a[i+1] - a[i] > 15:
        duration += a[i] + 15
        break

print(duration if duration < 90 else 90)
