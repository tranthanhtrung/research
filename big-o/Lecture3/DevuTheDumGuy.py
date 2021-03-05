[n, x] = list(map(int, input().split()))
arr = list(map(int, input().split()))

time = 0
arr.sort()
for i in range(n):
    time += arr[i] * x
    if (x > 1):
        x -= 1

print(time)