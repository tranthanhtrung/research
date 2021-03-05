n = int(input())
cards = list(map(int, input().split()))

l = 0
r = n - 1

result = [0,0]
i = 0
while l <= r:
    if cards[l] > cards[r]:
        result[i%2] += cards[l]
        l += 1
    else:
        result[i%2] += cards[r]
        r -= 1
    i += 1

print(result[0], result[1])
