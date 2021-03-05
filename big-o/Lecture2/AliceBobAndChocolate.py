n = int(input())
chocolate = list(map(int, input().split()))

l = 0
r = n - 1
time_l = 0
time_r = 0
while l <= r:
    if time_l + chocolate[l] <= time_r + chocolate[r]:
        time_l += chocolate[l]
        l += 1
    else:
        time_r += chocolate[r]
        r -= 1

print(l, n - l)