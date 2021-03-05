[n, m] = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

k = 0
for i in range(0, m):
    if k < n and b[i] >= a[k]:
        k +=  1

print(len(a) - k)
