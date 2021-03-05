_ = input()
chose = list(map(int, input().split()))
a1 = list(map(int, input().split()))
a2 = list(map(int, input().split()))

if a1[chose[0] - 1] < a2[len(a2) - chose[1]]:
    print("YES")
else:
    print("NO")
